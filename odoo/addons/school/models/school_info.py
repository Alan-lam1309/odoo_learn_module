from odoo import models, fields

class SchoolInfomation(models.Model):
    _name = "school.info"
    _description = 'School Management'

    name = fields.Char(string='Tên Trường')
    type = fields.Selection([('private','Dân lập'),('public','Công lập')], String="Loại trường", default='public')
    email = fields.Text(String='Email')
    address = fields.Text(String='Address')