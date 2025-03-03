from Models.Base import *
class Roles(Base):
    id = PrimaryKeyField
    role_name = CharField()

if __name__ == "__main__":
    connect().create_tables([Roles])