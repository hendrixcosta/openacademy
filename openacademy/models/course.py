from openerp import models, fields, api


class course(models.Model):


    _name = "openacademy.course"
    _description = "Course"


    name = fields.Char(
        string="Titulo",
        required=True
    )

    description = fields.Char(
        string="Descricao"
    )



    responsible_id = fields.Many2one('res.users')

    session_ids = fields.One2many('openacademy.session', 'name')

    display_name = fields.Char(compute='_compute_display_name')


    session_ids = fields.One2many('openacademy.session', 'course_id')

    @api.one
    @api.depends('name', 'description')     # this definition is recursive
    def _compute_display_name(self):
        if self.description:
            self.display_name = self.name   + ' / ' + self.description
        else:
            self.display_name = self.name
