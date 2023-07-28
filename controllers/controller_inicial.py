from flask import render_template, Blueprint, request, redirect, session
from database.models import User
from database.database import Database, select
from utils.utils import hash_password, encoded_password


bp = Blueprint(
    'login',
    __name__,
    template_folder='templates'
)


@bp.route('/')
def abrir_pagina_login():
        return render_template('login.html')


@bp.route('/register', methods=['POST'])
def abrir_registro():
    try:
        password_hash = hash_password(request.form['password'])
        print(password_hash)
        if request.method == 'POST':
            user = User(
                nome = request.form['nome'],
                email = request.form['email'],
                password = password_hash,
            )

            Database().run_insert(user)
        return render_template("login.html")

    except Exception as e:
        return f'email ja cadastrado na base!!!'




# renderizar rotas das paginas

@bp.route('/register')
def abrir_pagina_registro():
    return render_template('register.html')



@bp.route('/inicial', methods=['POST', 'GET'])
def abrir_pagina_inicial_autheticada():

    if request.method == 'GET':
         return render_template('inicial.html')
    
    try:
        query = select(User).where(User.email==request.form['email'])
        user: User = Database().get_one(query)

        password = user.password
        password_data = request.form['password']
        validate_password = encoded_password(password_data, password)

        if validate_password is not False:
            session['user'] = request.form['email']
            print(session)
            return redirect('/inicial')
        else:
            return redirect('/')
    except Exception as e:
        return redirect('/login')
    

@bp.route('/logout')
def signout():
    session.pop('user', None)
    print(session)
    return redirect('/')
