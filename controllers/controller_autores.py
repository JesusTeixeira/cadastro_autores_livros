from flask import request, render_template, redirect, Blueprint, session
from database.models import Autores
from database.database import Database, select

bp = Blueprint(
    'autores',
    __name__,
    template_folder='templates',
    url_prefix= '/autores' 
)

class AutoresCtrl:
    @bp.route('/editar/<int:id>', methods=['POST'])
    def editar_autor(id):
        query = select(Autores).where(Autores.id==id)
        autor: Autores = Database().get_one(query)

        if data := request.form:
                autor.nome = data['nome']
                autor.email = data['email']
                autor.nome_do_livro = data['nome_do_livro']

                Database().run_insert(autor)
                return redirect("/autores/listagem")

    @bp.route('/adicionar', methods=['POST'])
    def adicionar_autor():
        if request.method == 'POST':
            autor = Autores(
                nome = request.form['nome'],
                email = request.form['email'],
                nome_do_livro = request.form['nome_do_livro']
            )
        
            Database().run_insert(autor)
            return redirect("/autores/listagem")

@bp.route('/deletar/<int:id>', methods=['POST'])
def deletar_autor(id):
    if request.method == 'POST':
        query = select(Autores).where(Autores.id==id)
        autor = Database().get_one(query)
        Database().run_delete(autor)
    return redirect("/autores/listagem")

# rotas das paginas

@bp.route('/listagem')
def abrir_listagem_autores():
    if session:
        query = select(Autores)
        autores = Database().get_all(query)
        return render_template('autores/listagem.html', autores=autores)
    else:
        return redirect('/')

@bp.route('/cadastro')
def abrir_pagina_cadastro():
    return render_template('autores/cadastro.html')

@bp.route('/editar/<int:id>')
def abrir_pagina_edicao(id):
    query = select(Autores).where(Autores.id==id)
    autor = Database().get_one(query)
    return render_template('autores/editar.html', autor=autor)

@bp.route('/deletar/<int:id>')
def abrir_delete_registro(id):
    query = select(Autores).where(Autores.id==id)
    autor = Database().get_one(query)
    return render_template('autores/listagem.html', autor=autor)