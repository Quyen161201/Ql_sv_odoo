from odoo import models,fields,api

class Wizardstudent(models.TransientModel):
        _name = 'wizard.student'
        name = fields.Char('name')
        student_id = fields.Many2one('quanlysinhvien.student',string='Sinh viên')
        reason = fields.Text('Lý do')


        def btn_reason_student(self):
                if self.student_id:
                        self.student_id.reason=self.reason
                        self.student_id.status ='stop_studying'
