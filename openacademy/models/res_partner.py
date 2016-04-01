from openerp import models
from openerp import fields


class Partner (models.Model):

    _inherit = 'res.partner'


    is_instructor = fields.Boolean(
       "Instructor", default=False
    )

    session_ids = fields.One2many(
        'openacademy.session', 'instructor_id',
        string="Sessions"
    )

#    teacher_category = fields.Selection (
#        selection=[
#            ('leval1', 'Level 1'),
#            ('leval2', 'Level 2'),
#        ],
#        string='Teacher Category',
#    )
    teacher_category = fields.Char(
        string="Categoria"
    )
