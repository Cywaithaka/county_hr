from odoo import models, fields


class County(models.Model):
    _name = 'county'
    _description = 'County'

    name = fields.Char(string='County Name', required=True)
    description = fields.Text(string='Description')


class Subcounty(models.Model):
    _name = 'subcounty'
    _description = 'Subcounty'

    name = fields.Char(string='Subcounty Name', required=True)
    description = fields.Text(string='Description')
    county_id = fields.Many2one('county', string='County', required=True)

class Location(models.Model):
    _name = 'location'
    _description = 'Location'

    name = fields.Char(string='Location Name', required=True)
    description = fields.Text(string='Description')
    subcounty_id = fields.Many2one('subcounty', string='Subcounty', required=True)

class Village(models.Model):
    _name = 'village'
    _description = 'Village'

    name = fields.Char(string='Village Name', required=True)
    description = fields.Text(string='Description')
    location_id = fields.Many2one('location', string='Location', required=True)
