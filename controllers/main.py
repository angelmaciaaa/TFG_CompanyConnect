from odoo import http, _
from odoo.http import request
from odoo.tools import float_round

class HrAttendance(http.Controller):

    @staticmethod
    def _get_employee_info_response(employee):
        response = {}
        if employee:
            response = {
                'id': employee.id,
                'employee_name': employee.name,
                'employee_avatar': employee.image_1920,
                'hours_today': float_round(employee.hours_today, precision_digits=2),
                'last_check_in': employee.last_check_in,
                'attendance_state': employee.attendance_state,
                'use_pin': employee.company_id.attendance_kiosk_use_pin,
                'display_systray': employee.company_id.attendance_from_systray,
                'display_overtime': employee.company_id.hr_attendance_display_overtime
            }
        return response

    @http.route('/hr_attendance/employee_info', type='json', auth='public')
    def get_employee_info(self, employee_id):
        employee = request.env['hr.employee'].sudo().browse(employee_id)
        return self._get_employee_info_response(employee)

    @http.route('/hr_attendance/attendance_check_in', type='json', auth='public')
    def attendance_check_in(self, employee_id):
        employee = request.env['hr.employee'].sudo().browse(employee_id)
        employee.attendance_action_check_in()
        return self._get_employee_info_response(employee)

    @http.route('/hr_attendance/attendance_check_out', type='json', auth='public')
    def attendance_check_out(self, employee_id):
        employee = request.env['hr.employee'].sudo().browse(employee_id)
        employee.attendance_action_check_out()
        return self._get_employee_info_response(employee)