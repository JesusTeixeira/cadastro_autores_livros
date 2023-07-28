from flask import jsonify, Blueprint, jsonify, request, redirect
from lista_dict_livros import livros

bp = Blueprint(
    'livros_api',
    __name__,
    template_folder='templates' 
)

ROUTE = '/api/livros'

@bp.route(f'{ROUTE}', methods=['GET']) 
def get_books():
    return jsonify(livros)

@bp.route(f'{ROUTE}/<int:id>', methods=['GET']) 
def get_id_books(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
@bp.route(f'{ROUTE}/<int:id>', methods=['PUT']) 
def altered_book_by_id(id):
    altered_book = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(altered_book)
            return jsonify(livros[indice])
        

@bp.route(f'{ROUTE}', methods=['POST']) 
def add_new_book():
    livros.append(request.get_json())
    return jsonify(livros)

@bp.route(f'{ROUTE}/<int:id>', methods=['DELETE']) 
def delete_book_by_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
