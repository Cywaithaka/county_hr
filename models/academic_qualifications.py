from odoo import models, fields


class AcademicQualification(models.Model):
    _name = 'academic.qualification'
    _description = 'Academic Qualification'

    human_resource_id = fields.Many2one('human.resource', string='Resource', required=True)
    degree = fields.Char(string='Certification', required=True)  # ToDo this should be a many2one to registered institutions
    institution = fields.Char(string='Institution', required=True)  #ToDo this should be a many2one to registered institutions
    # start_date = fields.Date(string='Admission Date', required=True)
    # completion_date = fields.Date(string='Completion Date ', required=True)
    year = fields.Char(string='Year', required=True)
