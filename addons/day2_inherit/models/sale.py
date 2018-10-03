from odoo import models, fields, api

# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
#     sub_total_delivered = fields.Integer(string='Sub Total Delivered')

class SaleReport(models.Model):
    _inherit = 'sale.order.line'
    sub_delivered = fields.Integer(string='Sub Total Delivered')