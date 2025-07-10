from odoo import http
from odoo.http import request, Response
import json

class LibraryController(http.Controller):
    
    @http.route('/library/hello', auth='public', type='http', methods=['GET'], csrf=False)
    def hello_world(self, **kwargs):
      return Response(
        json.dumps({'message': 'Hello World!'}),
        content_type='application/json;charset=utf-8',
        status=200
      )

    @http.route('/books', auth='public', type='http', methods=['GET'], csrf=False)
    def get_books(self, **kwargs):
        books = request.env['library.book'].search([])
        book_list = []
        
        for book in books:
            book_list.append({
              'id': book.id,
              'name': book.name,
              'isbn': book.isbn,
              'state': book.state,
              'date_publisher': str(book.date_publisher) if book.date_publisher else None,
              'author_ids': book.author_ids.ids if book.author_ids else None,
              'publisher_id': book.publisher_id.id if book.publisher_id else None
            })

        return Response(
          json.dumps(book_list),
          content_type='application/json;charset=utf-8',
          status=200
        )