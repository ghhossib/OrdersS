from Models.Users import *
from bcrypt import hashpw, gensalt, checkpw


class UsersController:
    # метод вывода всех записей таблицы статусы

    @classmethod
    def show(cls, id):
        return Users.get_or_none(id)

    @classmethod
    def show_login(cls, login):
        return Users.get_or_none(Users.login == login)

    @classmethod
    def get(cls):
        return Users.select()

    # @classmethod
    # def registration(cls, login, password):
    #     try:
    #         hash_password = hashpw(password.encode('utf-8'), gensalt())
    #         Users.create(login=login, password=hash_password, role_id=3)
    #     except Exception as error:
    #         print(error)
    #         return False
    @classmethod
    def registration(cls, login, password):
        # Проверяем, существует ли пользователь с таким логином
        if Users.select().where(Users.login == login).exists():
            return False  # Пользователь с таким логином уже существует

        try:
            hash_password = hashpw(password.encode('utf-8'), gensalt())
            Users.create(login=login, password=hash_password, role_id=3)
            return True  # Пользователь успешно создан
        except Exception as error:
            print(error)
            return False  # Произошла ошибка при создании пользователя
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

    #print(UsersController.registration('ddd','ddd'))
    #for row in UsersController.get():
        #print(row.id, row.login,row.password, row.role_id)

    # print(UsersController.show(4))
    print(UsersController.auth('ddd','ddd'))