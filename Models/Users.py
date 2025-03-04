from Models.Base import *
from Models.Roles import Roles


class Users(Base):
    id = PrimaryKeyField
    login = CharField()
    password = CharField()
    role_id = ForeignKeyField(Roles)

if __name__ == "__main__":
    pass