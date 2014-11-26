# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################



from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools.safe_eval import safe_eval as eval
import openerp.addons.decimal_precision as dp

class product_product(osv.osv):
    _inherit = "product.product"
    
    _columns = {
                'framework':fields.selection([('Medication','Medication'),('Merchandise','Merchandise'),('Service','Service'),('Template','Template')], 'Framework'),
                'schedule':fields.integer('Schedule'),
                'tag_commisionable':fields.boolean('TagCommisionable'),
                'dogs':fields.boolean('Dogs'),
                'cats':fields.boolean('Cats'),
                'horse':fields.boolean('Horse'),
                'cattle':fields.boolean('Cattle'),
                'birds':fields.boolean('Birds'),
                'swine':fields.boolean('Swine'),
                'small_mammals':fields.boolean('Rabits Rodents small mammals'),
                'ferrets':fields.boolean('Ferrets'),
                'liamas':fields.boolean('Liamas'),
                'reptiles':fields.boolean('Reptiles'),
                'camel_ides':fields.boolean('Camel Ides'),
                'zoo_exotic':fields.boolean('Zoo Exotic'),
                'goats':fields.boolean('Goats'),
                'investigation_type':fields.selection([('Antech-Refrence','Antech-Refrence'),('Idexx-Refrence','Idexx-Refrence')], 'Investigation Type'),
                
                
                }