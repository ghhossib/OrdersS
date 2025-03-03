from Models.Users import *
from bcrypt import *


class UsersController:
    # метод вывода всех записей таблицы статусы

    @classmethod
    def show(cls, id):
        return Users.get_or_none(id)

    @classmethod
    def show_login(cls, login):
        return Users.get_or_none(Users.login == login)

    def get(cls):
        return Users.select()

    @classmethod
    def registration(cls, login, password, role):
        hash_password = hashpw(password.encode('utf-8'), gensalt())
        Users.create(login=login, password=hash_password, role=role)

    @classmethod
    def auth(cls,login,password):
        if Users.get_or_none(Users.login == login) != None:
            hspassword = Users.get_or_none(Users.login == login).password

            if checkpw(password.encode('utf-8'),hspassword.encode('utf-8')):
                return True
            return False

    @classmethod
    def update(cls,id,**filds):

        for key, value in filds.items():
            if key == 'password':
                value = hashpw(value.encode('utf-8'), gensalt())

            Users.update({key:value}).where(Users.id == id).execute()

    @classmethod
    def delete(cls, id):
        Users.delete_by_id(id)


if __name__ == "__main__":
    UsersController.registration('asdas',123,2)



