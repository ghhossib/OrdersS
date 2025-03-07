
from bcrypt import *

from flask import Flask, render_template, request, redirect
from Controllers.UserController import UsersController
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

# создать объект класса Flask
application = Flask(__name__)
application.secret_key = "BOOM"
# это объект управляет авторизацией
login_manager = LoginManager(application)
@login_manager.user_loader
def user_loader(id):
    return UsersController.show(int(id))




#Добавить методы работы с данными POST и GET
@application.route('/',methods = ['POST', 'GET'])

@application.route('/')
def home():
    title = "Вход"
    message = ''
    #переменной логин передается строка из формы
    login = request.form.get('login')
    password = request.form.get('password')
    #Проверка метода
    if request.method == 'POST':
       if UsersController.auth(login, password):
           login_user(UsersController.show_login(login))
           if UsersController.show_login(login).role == 'Administrator':
                return redirect('/admin')
           elif UsersController.show_login(login).role == 'Manager':
                return redirect('/manager')
           else:
                return redirect('/analyst')
    else:
           message = 'неверный логин или пароль'
    return render_template('login.html',
                           title = title,
                           message = message

                            )



@application.route('/admin',methods=['GET','POST'])
@login_required
def admin():
    title = "Админ панель"
    # Услови при котором открывается страница admin
    if current_user.role == "Администратор":
        users = UsersController.get()

        if request.method == 'POST':
            login = request.form.get('login')
            role = request.form.get('role')

            UsersController.registration(login, '123', role)
            return redirect('/admin')

        return render_template('admin_panel.html',
                           title = title, users=users)
    else:
        return redirect('/logout')

if __name__ == "__main__":
    application.run(debug=True)

