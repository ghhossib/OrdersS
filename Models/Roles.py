from Models.Base import *
class Roles(Base):
    id = PrimaryKeyField
    role_name = CharField()
    class Meta:
        table_name = 'roles'

if __name__ == "__main__":
    pass