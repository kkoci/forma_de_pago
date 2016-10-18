# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import fields as old_fields
from openerp.exceptions import except_orm, Warning
import openerp.addons.decimal_precision as dp

class forma_pago(models.Model):
    _name = 'forma_pago'
    _rec_name = 'forma_de_pago'

    forma_de_pago = fields.Char(string="Forma de Pago")
	
class account_invoice(models.Model):
    _inherit = "account.invoice"

    payment_method = fields.Many2one(comodel_name="forma_pago", string="Forma de Pago")