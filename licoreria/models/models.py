# -*- coding: utf-8 -*-

from odoo import models, fields, api

class licoreria_categoria(models.Model):
	_name = "licoreria.categoria"

	name = fields.Char(string = "Nombre", required=True, help="Introduce el nombre de la categoria")
	description = fields.Char(string = "Description")
	tipo = fields.Selection([('0','Destilada'),('1','Fermentada'),('2','Fortificada'),('3','Licores')], string="Tipo", default="0")
	bebidas = fields.One2many("licoreria.bebida", "categoria", string="Bebidas")

class licoreria_bebida(models.Model):
	_name = "licoreria.bebida"

	name = fields.Char(string = "Marca", required=True,help="Introduce la Marca de la bebida")
	precio = fields.Float(string="Precio")
	grados = fields.Float(string="Grados")
	ejemplares = fields.Integer(string = "Ejemplares")
	categoria = fields.Many2one("licoreria.categoria", string="categoria", required=True)	
	importetotal =fields.Float(string="Importe Total", compute="_importetotal", store=True)

	@api.depends('precio','ejemplares')
	def _importetotal(self):
		for r in self:
			r.importetotal = r.ejemplares * r.precio


# class licoreria(models.Model):
#     _name = 'licoreria.licoreria'
#     _description = 'licoreria.licoreria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
