from odoo import models,fields,api


class Student(models.Model):
    _name = 'quanlysinhvien.student'
    _description = 'Sinh viên'
    name = fields.Char('Tên sinh viên', required=True)
    date = fields.Date('Ngày sinh')
    sex = fields.Selection([('nam','Nam'),('nu','Nữ')],string='Giới tính', default = 'nam')
    address = fields.Text('Địa chỉ')
    phone = fields.Char('Số điện thoại')
    class_id = fields.Many2one('quanlysinhvien.class',string='Lớp')
    status = fields.Selection([('studing','Đang học'),('graduated','Đã tốt nghiệp'),('stop_studying','Bỏ học')], default='studing',string="Trạng thái")
    reason = fields.Text('Lý do buộc thôi học')

    def check_status_studing_student(self):
        self.status='studing'

    def check_status_graduated_student(self):
        self.status = 'graduated'