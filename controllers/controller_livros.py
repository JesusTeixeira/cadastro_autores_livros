from flask import request, render_template, redirect, Blueprint, session
from database.models import Livros
from database.database import Database, select


bp = Blueprint(
    'livros',
    __name__,
    template_folder='templates',
    url_prefix = '/livros'
)

class LivrosCtrl:
    @bp.route('/editar/<int:id>', methods=['POST'])
    def editar_livro(id):
        query = select(Livros).where(Livros.id==id)
        livro: Livros = Database().get_one(query)
        try:
            if data := request.form:
                livro.titulo = data['titulo']
                livro.autor = data['autor']

                Database().run_update(livro)
                return redirect("/livros/listagem")
  
        except Exception as e:
            return f'Livro não encontrado'


    @bp.route('/adicionar', methods=['POST'])
    def adicionar_livro():
        if request.method == 'POST':
            livro = Livros(
                titulo = request.form['titulo'],
                autor = request.form['autor'],
            )


            Database().run_insert(livro)
            return redirect("/livros/listagem")

    @bp.route('/deletar/<int:id>', methods=['POST', 'DELETE'])
    def deletar_livro(id):
        if request.method == 'POST':
            query = select(Livros).where(Livros.id==id)
            livro = Database().get_one(query)
            Database().run_delete(livro)
        return redirect("/livros/listagem")


# renderizar rotas das paginas

@bp.route('/listagem') 
def abrir_listagem_livros():
    if session:
        query = select(Livros)
        livros = Database().get_all(query)
        return render_template('livros/listagem.html', livros=livros)
    else:
        return redirect('/')

@bp.route('/cadastro')
def abrir_pagina_cadastro():
    if session:
        return render_template('livros/cadastro.html')
    else:
        return redirect('/')

@bp.route('/editar/<int:id>')
def abrir_pagina_edicao(id):
    if session:
        query = select(Livros).where(Livros.id==id)
        livro = Database().get_one(query)
        return render_template('livros/editar.html', livro=livro)
    else:
        return redirect('/')

@bp.route('/deletar/<int:id>')
def abrir_delete_registro(id):
    query = select(Livros).where(Livros.id==id)
    livro = Database().get_one(query)
    return render_template('livros/listagem.html', livro=livro)