# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json

class LibraryController(http.Controller):

    @http.route('/library/books', auth='public', type='http', methods=['GET'], csrf=False)
    def get_books(self, **kwargs):
        books = request.env['library.book'].search([])
        book_list = []

        for book in books:
            book_list.append({
                'id': book.id,
                'name': book.name,
                'isbn': book.isbn,
                'state': book.state,
                'date_published': str(book.date_published) if book.date_published else None,
                'author_id': book.author_id.id if book.author_id else None,
                'publisher_id': book.publisher_id.id if book.publisher_id else None
            })

        return Response(
            json.dumps(book_list),
            content_type='application/json;charset=utf-8',
            status=200
        )

    @http.route('/library/books/<int:book_id>', auth='public', type='http', methods=['GET'], csrf=False)
    def get_book(self, book_id, **kwargs):
        book = request.env['library.book'].browse(book_id)
        if not book.exists():
            return Response(
                json.dumps({'error': 'Book not found'}),
                content_type='application/json;charset=utf-8',
                status=404
            )

        book_data = {
            'id': book.id,
            'name': book.name,
            'isbn': book.isbn,
            'state': book.state,
            'date_published': str(book.date_published) if book.date_published else None,
            'author_id': book.author_id.id if book.author_id else None,
            'author_name': book.author_id.name if book.author_id else None,
            'publisher_id': book.publisher_id.id if book.publisher_id else None,
            'publisher_name': book.publisher_id.name if book.publisher_id else None
        }

        return Response(
            json.dumps(book_data),
            content_type='application/json;charset=utf-8',
            status=200
        )