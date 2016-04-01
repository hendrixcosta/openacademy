from openerp import models, fields


class attendee(models.Model):

    _name = 'openacademy.attendee'
    _description = 'Model of Atendee'

    partner_id = fields.Many2one('res.partner')
    session_id = fields.Many2one('openacademy.session')

    name = fields.Char(
        string='Nome',
        required=False,
    )
