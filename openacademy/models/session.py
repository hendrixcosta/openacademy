from openerp import models
from openerp import fields


class session (models.Model):

    _name = 'openacademy.session'
    _description = 'Model de session'

    name = fields.Char (
        string="Nome",
        required=True,
    )

    description = fields.Char(
        string='Descricao do curso',
        related='course_id.description',
    )

    instructor_id = fields.Many2one(
        'res.partner',
        string="Instructor",
        domain=['|',('is_instructor', '=', True),('teacher_category', 'ilike', 'teacher')])
    #'|',('is_instructor', '=', True),

    course_id = fields.Many2one('openacademy.course')
    attendee_ids = fields.One2many('openacademy.attendee', 'name')

    start_date = fields.Date()
    duration = fields.Integer()
    seats = fields.Integer()


#    teacher_category = fields.Selection (
#        selection=[
#            ('leval1', 'Level 1'),
#            ('leval2', 'Level 2'),
#        ],
#        string='Teacher Category',
#    )
