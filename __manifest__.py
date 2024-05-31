# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'CompanyConnect',
    'version': '1.0',
    'category': 'Human Resources/Attendances',
    'sequence': 240,
    'summary': 'Track employee attendance',
    'description': """
This module aims to manage employee's attendances.
==================================================

Keeps account of the attendances of the employees on the basis of the
actions(Check in/Check out) performed by them.
       """,
    'author': 'Angel Macia',
    'website': 'https://www.odoo.com/app/employees',
    'depends': ['project', 'hr', 'barcodes'],
    'data': [
        'security/hr_attendance_security.xml',
        'security/project_todo_security.xml',
        'security/ir.model.access.csv',
        'data/mail_activity_type_data.xml',
        'data/todo_template.xml',
        'views/attendance_views.xml',
        'views/todo_views.xml',
        'views/company_connect_menus.xml',
        'views/todo_wizards_views.xml',
        'views/company_connect_templates.xml'
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'company_connect/static/src/**/*',
            'company_connect/static/src/components/attendance_menu/**/*',
            'company_connect/static/src/components/card_layout/**/*',
            'company_connect/static/src/components/manual_selection/**/*',
            'company_connect/static/src/components/greetings/**/*',
            'company_connect/static/src/components/pin_code/**/*',
            'company_connect/static/src/components/kiosk_barcode/**/*',
            'company_connect/static/src/components/todo_done_checkmark/**/*',
            'company_connect/static/src/components/todo_editable_breadcrumb_name/**/*',
            'company_connect/static/src/scss/todo.scss',
            'company_connect/static/src/views/**/*',
            'company_connect/static/src/web/**/*',
        ],
        'web.qunit_suite_tests': [
            'company_connect/static/tests/hr_attendance_mock_server.js',
        ],
        'web.qunit_mobile_suite_tests': [
            'company_connect/static/tests/hr_attendance_mock_server.js',
        ],
        'company_connect.assets_public_attendance': [
            # Front-end libraries
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_frontend_helpers'),
            'web/static/lib/jquery/jquery.js',
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_frontend'),
            ('include', 'web._assets_bootstrap_backend'),
            '/web/static/lib/odoo_ui_icons/*',
            '/web/static/lib/bootstrap/scss/_functions.scss',
            '/web/static/lib/bootstrap/scss/_mixins.scss',
            '/web/static/lib/bootstrap/scss/utilities/_api.scss',
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            ('include', 'web._assets_core'),

            # Public Kiosk app and its components
            "company_connect/static/src/public_kiosk/**/*",
            "company_connect/static/src/scss/hr_attendance.scss",
            #'company_connect/static/src/components/**/*', 
            #2024-05-29 17:51:05,240 18132 WARNING TFG-CompanyConnect odoo.addons.web.controllers.binary: Parsing asset bundle company_connect.assets_public_attendance.min.js 
            #has failed: Cannot create 'company_connect.TodoEditableBreadcrumbName' because the template to inherit 'web.CharField' is not found. 
            'company_connect/static/src/components/attendance_menu/**/*',
            'company_connect/static/src/components/card_layout/**/*',
            'company_connect/static/src/components/manual_selection/**/*',
            'company_connect/static/src/components/greetings/**/*',
            'company_connect/static/src/components/pin_code/**/*',
            'company_connect/static/src/components/kiosk_barcode/**/*',
            'company_connect/static/src/components/check_in_out/**/*',
            "web/static/src/views/fields/formatters.js",

            # Barcode reader utils
            "web/static/src/webclient/barcode/barcode_scanner.js",
            "web/static/src/webclient/barcode/barcode_scanner.xml",
            "web/static/src/webclient/barcode/barcode_scanner.scss",
            "web/static/src/webclient/barcode/crop_overlay.js",
            "web/static/src/webclient/webclient_layout.scss",
            "web/static/src/webclient/barcode/crop_overlay.xml",
            "web/static/src/webclient/barcode/crop_overlay.scss",
            "web/static/src/webclient/barcode/ZXingBarcodeDetector.js",
            "barcodes/static/src/components/barcode_scanner.js",
            "barcodes/static/src/components/barcode_scanner.xml",
            "barcodes/static/src/components/barcode_scanner.scss",
            "barcodes/static/src/barcode_service.js",

            # Kanban view mock
            "web/static/src/views/kanban/kanban_controller.scss",
            "web/static/src/search/search_panel/search_panel.scss",
            "web/static/src/search/control_panel/control_panel.scss",
        ]
    },
    'license': 'LGPL-3',
}
