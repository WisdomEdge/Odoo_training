# -*- coding: utf-8 -*-

from odoo import api, fields, models

# list of book
class book_list(models.Model):
    _name = "book_list"
    _description = "Book List"
    name = fields.Char("book_name")
    author = fields.Char("author")
    borrow_id = fields.Many2one('book_borrow')

#list of borrower
class book_borrower(models.Model):
    _name = "book_borrower"
    _description = "Book Borrower"
    name = fields.Char("name")
    age = fields.Char("age")

# list order to borrow
class book_borrow(models.Model):
    _name = "book_borrow"
    _description = "Book Borrow"
    borrower = fields.Many2one("book_borrower")
    list_book = fields.One2many("book_list", 'borrow_id')
