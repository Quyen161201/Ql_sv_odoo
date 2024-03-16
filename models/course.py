from odoo import fields, models, api


class Course(models.Model):
    _name = 'course'
    _description = 'Khóa học'

    name = fields.Char('Khóa học',required=True)
    start_year = fields.Date('Năm bắt đầu')
    end_year = fields.Date('Năm kết thúc')
