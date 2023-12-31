# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "my.pet"
    _description = "My pet model"

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    age = fields.Integer('Pet Age', default=1)
    weight = fields.Float('Weight (kg)')
    dob = fields.Date('DOB', required=False)
    basic_price = fields.Float('Basic Price', default=0)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                string="Related Products",
                                relation='pet_product_rel',
                                column1='col_pet_id',
                                column2='col_product_id')

    @api.model
    def create(self, vals):
        is_check_duplicated_pet_name = self.env['ir.config_parameter'].sudo().get_param(
            'mypet.is_check_duplicated_pet_name', default=False)
        if is_check_duplicated_pet_name:
            vals = [vals, ] if not isinstance(vals, (tuple, list)) else vals
            for val in vals:
                pet_name = val["name"]
                pet_records = self.search([('name', '=', pet_name)])
                if pet_records:
                    raise ValidationError(_("Duplicated pet name @ %s" % pet_name))