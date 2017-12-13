# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ynot_project(models.Model):
    _name = 'ynot.project'

    @api.one
    def _compute_currency(self):
        self.currency_id = self.company_id.currency_id


    name = fields.Char("Project Title", required=True)
    create_date = fields.Datetime('Created', readonly=True)
    create_uid = fields.Many2one('res.users', string='Completed By', readonly=True) 
    assigned_to = fields.Many2one('res.users', string='Assigned To',)
    assigned_date = fields.Date('Date')
    client_company_id = fields.Many2one('res.partner', string='Company', domain="[('customer','=',True),('is_company','=',True)]",
                                context="{'search_default_customer':1, 'show_address': 1}")
    client_id = fields.Many2one('res.partner', string='Client', domain="[('customer','=',True),('is_company','=',False)]",)
    revenue_opportunity = fields.Monetary(currency_field='currency_id', string="Revenue Opportunity")
    currency_id = fields.Many2one('res.currency', compute='_compute_currency', string="Currency")
    company_id = fields.Many2one('res.company', string='Company', store=True, readonly=True,
        default=lambda self: self.env['res.company']._company_default_get(''))

    price_range_from = fields.Monetary(currency_field='currency_id', string="Price Range From")
    price_range_to = fields.Monetary(currency_field='currency_id', string="Price Range To")

    project_overview = fields.Text("Project Overview")

    is_design = fields.Boolean(string='Design',)
    is_sourcing = fields.Boolean(string='Sourcing',)
    is_pricing = fields.Boolean(string='Pricing',)

    task_research = fields.Boolean(string='Research Product')
    task_concept = fields.Boolean(string='Concept & Presentations')
    task_quote_overseas = fields.Boolean(string='Quatation Overseas')
    task_quote_local = fields.Boolean(string='Quotation Local(USA)')
    task_artwork = fields.Boolean(string='Artwork')
    task_sample_req = fields.Boolean(string='Samples Requisition')
    task_sample_payment = fields.Boolean(string='Samples Payment')
    task_followup = fields.Boolean(string='Follow Up')
    task_cust_po = fields.Boolean(string='Customer PO or Contract')
    task_charges = fields.Boolean(string='Charges to Customer')


    task_concept_add = fields.Selection([('duplicate','Duplicate'),('graphic','Graphic'),('pacakaging','Pacakaging'),('product','Product'),('other','Other')], string="Concept Additional Info")
    task_quote_overseas_add = fields.Selection([('india','India'),('china','China'),('other','Other'),], string="Overseas Additional Info")
    task_overseas_other = fields.Char("Other Country")
    
    target_audience = fields.Text("Target Audience", help="The who, what, when, and where of the target customer base")
    campaign_look = fields.Text("Campaign Look & Feel")
    competitive_analysis = fields.Text("Competitive Analysis")

    pre_sketches = fields.Boolean("Sketches")
    pre_illustrations = fields.Boolean("Illustrations")
    pre_renedring = fields.Boolean("3D Rendering")

    pro_tl_date_1 = fields.Date("Date 1")
    pro_tl_date_2 = fields.Date("Date 2")
    pro_tl_date_3 = fields.Date("Date 3")
    pro_tl_date_4 = fields.Date("Date 4")

    pro_tl_text_1 = fields.Char("Projected Timeline Desc 1")
    pro_tl_text_2 = fields.Char("Projected Timeline Desc 2")
    pro_tl_text_3 = fields.Char("Projected Timeline Desc 3")
    pro_tl_text_4 = fields.Char("Projected Timeline Desc 4")


    imp_tl_date_1 = fields.Date("Date 1")
    imp_tl_date_2 = fields.Date("Date 2")
    imp_tl_date_3 = fields.Date("Date 3")
    imp_tl_date_4 = fields.Date("Date 4")

    imp_tl_text_1 = fields.Char("Important Timeline Desc 1")
    imp_tl_text_2 = fields.Char("Important Timeline Desc 2")
    imp_tl_text_3 = fields.Char("Important Timeline Desc 3")
    imp_tl_text_4 = fields.Char("Important Timeline Desc 4")


    other_desc = fields.Text("Other Info")
    client_contact_id = fields.Many2one('res.partner', string='Client',
                                context="{'show_phone': 1}")

    notes = fields.Text("Notes")
    images = fields.One2many('project.image', 'project_id', string='Images')

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100


class project_image(models.Model):
    _name = 'project.image'
    _order = 'sequence, id DESC'

    name = fields.Char('Name')
    description = fields.Text('Description')
    sequence = fields.Integer('Sequence')
    image = fields.Binary('Image')
    project_id = fields.Many2one('ynot.project', string='Project')
    

class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def name_get(self):
        # res = super(res_partner,self).name_get()
        res = super(res_partner, self).name_get()
        print("OR name_get------------res-----------",res)
        final_res = []
        
        for rec in res:
            name = rec[1]
            partner = self.browse(rec[0])

            if self._context.get('show_phone') and partner.phone:
                name = "%s <%s>" % (name, partner.phone)
            final_res.append((partner.id, name))
        print( "final_res-----------",final_res)
        return final_res