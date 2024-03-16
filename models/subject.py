from odoo import api, models, fields
from odoo.exceptions import ValidationError


class Subject(models.Model):
    _name = 'quanlysinhvien.subject'
    name = fields.Char('Môn học')
    point_ids = fields.One2many('quanlysinhvien.point', 'subject_id', 'Điểm')

