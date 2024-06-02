# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _, _lt, Command, fields
from odoo.tools import html2plaintext
from datetime import datetime

class Task(models.Model):
    _inherit = 'project.task'

    timer_start = fields.Datetime(string='Timer Start')
    time_spent = fields.Float(string='Time Spent', compute='_calculate_time', store=True)
    timer = fields.Boolean("Timer Running", default=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') and not vals.get('project_id') and not vals.get('parent_id'):
                if vals.get('description'):
                    # Generating name from first line of the description
                    text = html2plaintext(vals['description'])
                    name = text.strip().replace('*', '').partition("\n")[0]
                    vals['name'] = (name[:97] + '...') if len(name) > 100 else name
                else:
                    vals['name'] = _('Untitled to-do')
        return super().create(vals_list)

    def _ensure_onboarding_todo(self):
        if not self.env.user.has_group('company_connect.group_onboarding_company_connect_todo'):
            self._generate_onboarding_todo(self.env.user)
            onboarding_group = self.env.ref('company_connect.group_onboarding_company_connect_todo').sudo()
            onboarding_group.write({'users': [Command.link(self.env.user.id)]})

    def _generate_onboarding_todo(self, user):
        user.ensure_one()
        body = self.with_context(lang=user.lang or self.env.user.lang).env['ir.qweb']._render(
            'company_connect.company_connect_todo_user_onboarding',
            {'object': user},
            minimal_qcontext=True,
            raise_if_not_found=False
        )
        if not body:
            return
        title = _lt('Welcome %s!', user.name)
        self.env['project.task'].create([{
            'user_ids': user.ids,
            'description': body,
            'name': title,
        }])

    def action_convert_to_task(self):
        self.ensure_one()
        self.company_id = self.project_id.company_id
        return {
            'view_mode': 'form',
            'res_model': 'project.task',
            'res_id': self.id,
            'type': 'ir.actions.act_window',
        }
    
    def _start(self):
        self.ensure_one()
        if not self.timer:
            self.timer_start = datetime.now()
            self.timer = True

    def action_start(self):
        self._start()

    def _stop(self):
        self.ensure_one()
        if self.timer:
            delta = datetime.now() - fields.Datetime.from_string(self.timer_start)
            self.time_spent += delta.total_seconds() / 3600
            self.timer = False
        self.timer_start = False
        
    def action_stop(self):
        self._stop()

    @api.depends('timer_start', 'timer')
    def _calculate_time(self):
        for task in self:
            if task.timer and task.timer_start:
                delta = datetime.now() - fields.Datetime.from_string(task.timer_start)
                task.time_spent += delta.total_seconds() / 3600
                task.timer_start = fields.Datetime.now()

    def write(self, vals):
        for task in self:
            if 'stage_id' in vals:
                new_stage = self.env['project.task.type'].browse(vals['stage_id'])
                new_state = new_stage.name if new_stage else False
                if new_state:
                    if new_state == 'In Progress':
                        task._start_timer()
                    elif new_state in ['Changes Requested', 'Waiting', 'Cancelled', 'Done']:
                        task._stop_timer()
        return super(Task, self).write(vals)


class MailActivityType(models.Model):
    _inherit = "mail.activity.type"

    category = fields.Selection(selection_add=[('reminder', 'Reminder')])