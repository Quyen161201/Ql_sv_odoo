from odoo import models,fields,api
from odoo.exceptions import ValidationError
class Department(models.Model):
    _name = 'department'
    name = fields.Char('Tên khoa', required=True)
    year = fields.Date ('Năm thành lập')
    class_ids = fields.One2many('quanlysinhvien.class','department_id','Lớp')

    @api.constrains('name')
    def _check_name_department(self):

            if self.search([('name', '=', self.name), ('id', '!=', self.id)]):
              raise ValidationError('Tên khoa đã tồn tại')

