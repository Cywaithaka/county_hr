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

    @api.onchange("village_id")
    def onchange_village_id(self):
        for record in self:
            village = record.village_id
            if not record.location_id and village and village.location_id:
                record.location_id = village.location_id.id

    @api.onchange("location_id")
    def onchange_location_id(self):
        res = {}
        for record in self:
            location = record.location_id
            if not record.subcounty_id and location and location.subcounty_id:
                record.subcounty_id = location.subcounty_id.id
            if location:
                res["domain"] = {"village_id": [("location_id", "=", location.id)]}
        return res

    @api.onchange("subcounty_id")
    def onchange_subcounty_id(self):
        res = {}
        for record in self:
            subcounty = record.subcounty_id
            if not record.county_id and subcounty and subcounty.county_id:
                record.county_id = subcounty.county_id.id
            if subcounty:
                res["domain"] = {"location_id": [("subcounty_id", "=", subcounty.id)]}
        return res

    @api.onchange("county_id")
    def onchange_county_id(self):
        res = {}
        for record in self:
            county = record.county_id
            if county:
                res["domain"] = {"subcounty_id": [("county_id", "=", county.id)]}
        return res
