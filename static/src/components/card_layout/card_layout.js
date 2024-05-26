/** @odoo-module **/

import { Component } from "@odoo/owl";

export class CardLayout extends Component {}

CardLayout.template = "company_connect.CardLayout";
CardLayout.props = {
    kioskModeClasses: { type: String, optional: true },
    slots: Object,
};
CardLayout.defaultProps = {
    kioskModeClasses: "",
};
