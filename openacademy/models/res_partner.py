from openerp import models
from openerp import fields


class ResPartner (models.Model):

    _inherit = 'res.partner'
    _name = 'openacademy.respartner'

    is_instructor = fields.Boolean(
        string="Instrutor"
    )

