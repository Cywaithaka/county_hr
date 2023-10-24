from odoo import models, fields, api


class HumanResource(models.Model):
    _name = 'human.resource'
    _description = 'Human Resource'

    name = fields.Char(string='Applicant Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone', required=True)
    address = fields.Text(string='Address')
    passport_photo = fields.Image("Passport Photo", attachment=True, max_width=1920, max_height=1920)
    active = fields.Boolean('Active', default=True)
    documents = fields.Many2many('ir.attachment', 'hr_attachment_rel', 'applicant_id', 'attachment_id',
                                 string='Documents', help="Attach CV and other academic documents")
    county_id = fields.Many2one('county', string='County')
    subcounty_id = fields.Many2one('subcounty', string='Subcounty')
    location_id = fields.Many2one('location', string='Location')
    village_id = fields.Many2one('village', string='Village')
    qualifications = fields.One2many('academic.qualification', 'human_resource_id', string='Academic Qualifications')
