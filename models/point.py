from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Point(models.Model):
    _name = 'quanlysinhvien.point'
    name = fields.Float('Điểm',group_operator="avg")
    student_id = fields.Many2one('quanlysinhvien.student', string='Sinh viên')
    subject_id = fields.Many2one('quanlysinhvien.subject', string='Môn học')
    status = fields.Selection([('pass','Qua môn'),('retest','Thi lại')],string='Trạng thái',compute='_check_point_student', store=True)
    sum_point = fields.Float('Tổng điểm', compute='_average_point' )
    @api.model
    def create(self, vals):
        if self.search([('student_id', '=', vals['student_id']), ('subject_id', '=', vals['subject_id'])]):
            raise ValidationError('Tên môn hoc đã tồn tại')
        return super(Point, self).create(vals)

    @api.model
    def write(self, vals):

        if 'subject_id' in vals:
            if self.search([('subject_id','=',vals['subject_id'])]):
                raise  ValidationError('Tên môn học đã tồn tại')
        elif 'student_id' in vals and 'subject_id' in vals:
            if self.search([('student_id','=',vals['student_id']),('subject_id','=',vals['subject_id'])]):
                raise  ValidationError('Tên môn học đã tồn tại')
        elif 'student_id' in vals:

            if self.search([('student_id', '=', vals['student_id']), ('subject_id', '=', self.subject_id.id)]):
                raise ValidationError('Tên môn học đã tồn tại')
        return super().write(vals)

    @api.depends('name')

    def _check_point_student(self):

            if self.name >= 5 and self.name <= 10:
                self.status = 'pass'
            elif self.name < 5:
                self.status = 'retest'
            else:
                raise ValidationError('Điểm chỉ từ 0-10')

    @api.depends('name')
    def _average_point(self):
        count = len(self)
        sum = 0

        for rec in self:
            sum += rec.name


        self.sum_point = sum/count
        print('sum', sum)
        print('count',count)




