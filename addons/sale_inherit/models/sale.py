from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_invoice = fields.Char(string='Customer Invoice')