from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'quanlysinhvien.class'
    _description = 'lớp'

    name = fields.Char('Tên lớp', require=True)
    department_id = fields.Many2one('department', string='Khoa')
    course_id = fields.Many2one('course',string='Khóa học')
    student_ids = fields.One2many('quanlysinhvien.student','class_id','sinh viên')