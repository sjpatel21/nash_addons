# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ynot_project(models.Model):
    _name = 'ynot.project'

    @api.one
    def _compute_currency(self):
        self.currency_id = self.company_id.currency_id

    name = fields.Char("Project Title", required=True)
    create_date = fields.Datetime('Created', readonly=True)
    create_uid = fields.Many2one(
        'res.users', string='Completed By', readonly=True)
    assigned_to = fields.Many2one('res.users', string='Assigned To',)
    assigned_date = fields.Date('Date')
    client_company_id = fields.Many2one('res.partner', string='Company', domain="[('customer','=',True),('is_company','=',True)]",
                                        context="{'search_default_customer':1, 'show_address': 1}")
    client_id = fields.Many2one('res.partner', string='Client',
                                domain="[('customer','=',True),('is_company','=',False)]",)
    revenue_opportunity = fields.Monetary(
        currency_field='currency_id', string="Revenue Opportunity")
    currency_id = fields.Many2one(
        'res.currency', compute='_compute_currency', string="Currency")
    company_id = fields.Many2one('res.company', string='Company', store=True, readonly=True,
                                 default=lambda self: self.env['res.company']._company_default_get(''))

    price_range_from = fields.Monetary(
        currency_field='currency_id', string="Price Range From")
    price_range_to = fields.Monetary(
        currency_field='currency_id', string="Price Range To")

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

    task_concept_add = fields.Selection([('duplicate', 'Duplicate'), ('graphic', 'Graphic'), (
        'pacakaging', 'Pacakaging'), ('product', 'Product'), ('other', 'Other')], string="Concept Additional Info")
    task_quote_overseas_add = fields.Selection(
        [('india', 'India'), ('china', 'China'), ('other', 'Other'), ], string="Overseas Additional Info")
    task_overseas_other = fields.Char("Other Country")

    target_audience = fields.Text(
        "Target Audience", help="The who, what, when, and where of the target customer base")
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
        print("OR name_get------------res-----------", res)
        final_res = []

        for rec in res:
            name = rec[1]
            partner = self.browse(rec[0])

            if self._context.get('show_phone') and partner.phone:
                name = "%s <%s>" % (name, partner.phone)
            final_res.append((partner.id, name))
        print("final_res-----------", final_res)
        return final_res


class YnotFactory(models.Model):
    _name = 'ynot.factory'

    name = fields.Char(
        string='Company Name',
        required=True,
    )
    company_address = fields.Text(
        string='Company Address',
    )
    nearest_port = fields.Char("Nearest Port")
    major_airport = fields.Char("Nearest Major Airport")
    year_est = fields.Integer("Year Est")
    no_of_emp = fields.Integer("No. of Employees")
    loc_fun = fields.Text('Location or Functions')
    company_website = fields.Char("Company Website")
    company_cert = fields.Char("Company Certifications")
    ecommerce = fields.Char("Ecommerce")
    is_catelogs = fields.Boolean("Catalogs")
    catalog_updated = fields.Char("How often updated ?")

    # General Financial Info
    sale_ten_three = fields.Float("Sale from 10 Yrs Ago to Last 3 Yrs")
    sale_three_three = fields.Float("Sale from 3 Yrs Ago to Last 3 Yrs")
    sale_two_three = fields.Float("Sale from 2 Yrs Ago to Last 3 Yrs")
    sale_last_year = fields.Float("Sale from Last Year")

    # Government Licenses
    local_lic = fields.Char("Local")
    state_lic = fields.Char("State")
    federal_lic = fields.Char("Federal")

    # Shipping Info
    methods_shipping = fields.Char("Methods of Shipping")
    fob_ship = fields.Char("FOB")
    exworks_ship = fields.Char("EX-WORKS")

    # Clinet Info

    major_client_ids = fields.One2many(
        string='Major Clients',
        help="What percentage of their business is with each company; and which countries are these clients from",
        comodel_name='major.clients',
        inverse_name='factory_id',
    )

    top_country_ids = fields.Many2many(
        string='Top Country',
        comodel_name='res.country',
        relation='factory_top_country',
        column1='factory_id',
        column2='res_country_id',
    )

    # misc info
    sample_charges = fields.Char("Sample Charges (or Free)")
    con_orders = fields.Char("Consolidation of Orders")
    con_cont = fields.Char("Consolidation of Containers")
    prod_testing = fields.Char("Product Testing")
    is_prd_engg = fields.Boolean("Engineering")
    is_threed_modelling = fields.Boolean("3D Modelling")
    acceptable_formats = fields.Char("List of Acceptable Formats")
    is_accept_terms = fields.Boolean("Do you accept Y-Not's terms (listed)?")

    # Contact Info
    factory_contact_ids = fields.One2many(
        string='Factory Contacts',
        comodel_name='factory.contact',
        inverse_name='factory_id',
    )
    company_contact = fields.Char("Company Contact")
    sale_managers = fields.Char("Sale Managers")
    head_of_aperation = fields.Char("Head of Operations")
    c_level_position = fields.Char("C-Level Positions")
    owner = fields.Char("Owner(s)")

    # business info
    material_ids = fields.Many2many(
        string='Materials',
        comodel_name='factory.material',
        relation='factory_res_material',
        column1='factory_id',
        column2='material_id',
    )
    product_cat_ids = fields.Many2many(
        string='Product Categories/ Ranges',
        comodel_name='factory.prdcat',
        relation='factory_res_prdcat',
        column1='factory_id',
        column2='prdcat_id',
    )
    samples = fields.Text("Samples")
    sample_lead_time = fields.Char("Sample Lead Time")
    sample_prd_time = fields.Char("Production Lead Time")

    # internal use
    ynot_contact_person = fields.Many2one("res.users", "Y-not Contact Person")
    english = fields.Selection(
        string='English',
        selection=[('1', 'Very Low'), ('2', 'Low'),
                   ('3', 'Normal'), ('4', 'High'), ('5', 'Very High')]
    )
    cleanliness = fields.Selection(
        string='Cleanlinesss',
        selection=[('1', 'Very Low'), ('2', 'Low'),
                   ('3', 'Normal'), ('4', 'High'), ('5', 'Very High')]
    )


class YnotMaterial(models.Model):
    _name = 'factory.material'

    name = fields.Char("Material", required=True)


class YnotProductCat(models.Model):
    _name = 'factory.prdcat'

    name = fields.Char("Product Category", required=True)


class YnotMajorClient(models.Model):
    _name = 'major.clients'

    factory_id = fields.Many2one('ynot.factory', string='Factory',)
    name = fields.Char("Name", required=True)
    per_of_business = fields.Float("Percentage of Business")
    country_id = fields.Many2one('res.country', 'Country')


class YnotFactoryContact(models.Model):
    _name = 'factory.contact'

    factory_id = fields.Many2one('ynot.factory', string='Factory',)
    name = fields.Char("Contact Name", required=True)
    email = fields.Char("Email")
    office_phone = fields.Char("Office Phone")
    cell_phone = fields.Char("CellPhone")
    city = fields.Char("City")
    country_id = fields.Many2one('res.country', 'Country')
    
