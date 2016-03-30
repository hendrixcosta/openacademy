from openerp import models, fields, api


class course(models.Model):

    _name = "course.course"
    _description = "Course"
    _title = "Cousera"

    name = fields.Char(
        string="Name"
    )

    title = fields.Char(
        string="Titulo"
    )
    description = fields.Text(
        string="Descricao"
    )
