from odoo import fields, models

class ProductPet(models.Model):
    _name = 'product.pet'
    _inherits = {'my.pet':'my_pet_id'}
    _description = 'Product Pets'

    my_pet_id = fields.Many2one(
        'my.pet', 'My Pet',
        auto_join=True, index=True, ondelete="cascade", required=True
    )

    pet_type = fields.Selection([
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('vip', 'VIP'),
        ('cute', 'Cute'),
        ], String='Pet Type', default='basic')

    pet_color = fields.Selection([
        ('white', 'White'),
        ('yellow', 'Yellow'),
        ('gray', 'Gray'),
        ('black', 'Black'),
    ], String='Pet Color', default='white')

    bonus_price = fields.Float(String='Bonus Price', default=0)

    final_price = fields.Float(String='Final Price', compute='_compute_final_price')

    def _compute_final_price(self):
        for record in self:
            record.final_price = record.bonus_price + record.basic_price

