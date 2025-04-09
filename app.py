from itertools import product
from pyexpat.errors import messages

from bcrypt import *
from flask import Flask, render_template, request, redirect, session

from Controllers.ProductsController import ProductsController
from Controllers.UserController import UsersController
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from Models.Users import Users

# создать объект класса Flask
application = Flask(__name__)
application.secret_key = "BOOM"
# это объект управляет авторизацией
login_manager = LoginManager(application)
@login_manager.user_loader
def user_loader(id):
    return UsersController.show(int(id))

@application.route('/', methods=['POST', 'GET'])
def home():
    title = "Вход"
    message = ''
    login = request.form.get('login')
    password = request.form.get('password')

    if request.method == 'POST':
        if UsersController.auth(login, password):  # Если аутентификация успешна
            user = UsersController.show_login(login)
            login_user(user)
            if user is None:
                message = 'неверный логин или пароль'
            else:

                role_id = user.role_id.id  # Получаем числовой идентификатор роли
                if role_id == 1:  # Администратор
                    return redirect('/admin')
                elif role_id == 2:  # Менеджер
                    return redirect('/manager')
                else:  # Аналитик или другие роли
                    return redirect('/client')
        else:
            message = 'неверный логин или пароль'



    return render_template('login.html', title=title, message=message)


@application.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    title = "Админ панель"
    if current_user.role_id.id == 1:
        users = UsersController.get()

        if request.method == 'POST':
            login = request.form.get('login')
            password = request.form.get('password')
            role_id = request.form.get('role')

            print(f"Данные из формы: login={login}, password={password}, role_id={role_id}")

            if not login or not password or not role_id:
                return "Все поля должны быть заполнены", 400

            if UsersController.registration(login, password, role_id):
                return redirect('/admin')
            else:
                return "Ошибка при добавлении пользователя", 400

    else:
        return redirect('/logout')

    return render_template('admin_panel.html', title=title, users=users)


@application.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@application.route('/manager', methods=['GET','POST'])
@login_required
def manager():
        title = "Менеджер панель"
        return render_template('manager_panel.html',
                               title=title)

@application.route('/client', methods=['GET','POST'])
@login_required
def client():
        title = "Панель клиента"
        return render_template('clients_panel.html',
                               title=title)

@application.route('/client_catalog', methods=['GET','POST'])
@login_required
def client_catalog():
        title = "Каталог товаров"
        if current_user.role_id.id == 3:
            products = ProductsController.get()
        return render_template('catalog_products.html',
                               title=title,products=products)

@application.route('/client_delivery', methods=['GET','POST'])
@login_required
def client_delivery():
        title = "Каталог товаров"
        return render_template('delivery_status.html',
                               title=title)


@application.route('/test123', methods=['GET','POST'])
@login_required
def test123():
        title = "Каталог товаров"
        return render_template('test123.html',
                               title=title)

@application.route('/user/<int:id>', methods=['GET','POST'])
@login_required
def a_edit_panel(id):
        title = "Редактировать пользователя"
        if current_user.role_id.id == 1:
            user = UsersController.show(id)
            if request.method == 'POST':
                # получаем значения введеное в поле формы по имени fullname

                login = request.form.get('login')
                role_id = request.form.get('role_id')
                password = request.form.get('password')
                # передаю значения полей в метод обновления
                UsersController.update(id,login=login, password=password, role_id=role_id)

                # Возращение пользователя обратно после заполнения
                return redirect('/admin')

        return render_template('edit_admin-panel.html',
                               title=title, user=user)


#удаление пользователя
@application.route('/user/delete/<int:id>')
@login_required
def user_delete(id):
    if current_user.role_id.id == 1:
        UsersController.delete(id)
        return redirect('/admin')
    else:
        return redirect('/logout')


@application.route('/manger-edit_panel', methods=['GET','POST'])
@login_required
def m_edit_panel():
        title = "Редактировать товары"
        return render_template('edit_catalog_products.html',
                               title=title)

@application.route('/manger-edit_orders', methods=['GET','POST'])
@login_required
def m_edit_orders():
        title = "Редактировать заказы"
        return render_template('edit_orders.html',
                               title=title)



@application.route('/manger-email', methods=['GET','POST'])
@login_required
def m_email():
        title = "Отправить письмо"
        return render_template('email_notice.html',
                               title=title)


@application.route('/manger-catalog_products', methods=['GET','POST'])
@login_required
def m_catalog_products():
        title = "Редактировать каталог продуктов"
        return render_template('manager_catalog_products.html',
                               title=title)


@application.route('/manger-orders', methods=['GET','POST'])
@login_required
def m_orders():
        title = "Редактировать статус доставки"
        return render_template('manager_orders.html',
                               title=title)



@application.route('/manger-stocks', methods=['GET','POST'])
@login_required
def m_stocks():
        title = "Запасы"
        return render_template('manager_stocks.html',
                               title=title)


@application.route('/client-payment', methods=['GET','POST'])
@login_required
def c_payment():
        title = "Оплата заказа"
        return render_template('payment_products.html',
                               title=title)




# @application.route('/registration', methods=['GET','POST'])
# def registration():
#         title = "Регистрация"
#         message = ''
#         if request.method == 'POST':
#             login = request.form.get('login')
#             password = request.form.get('password')
#
#             if UsersController.registration(login, password):
#                 print('e')
#                 return redirect('/client')
#             else:
#                 print('a')
#                 message = 'Такой логин уже существует'
#
#
#
#
#         return render_template('registation.html',
#                                title=title, message=message)


@application.route('/registration', methods=['GET', 'POST'])
def registration():
    title = "Регистрация"
    message = ''
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if UsersController.registration(login, password):
            user = UsersController.show_login(login)  # Получаем пользователя
            if UsersController.auth(login, password):
                login_user(user)
                return redirect('/client')
            else:
                message = 'Ошибка авторизации после регистрации'
        else:
            message = 'Такой логин уже существует'

    return render_template('registation.html', title=title, message=message)





@application.route('/manager-reports', methods=['GET','POST'])
@login_required
def m_reports():
        title = "Формирование отчетов"
        return render_template('reports.html',
                               title=title)


if __name__ == "__main__":
    application.run(debug=True)