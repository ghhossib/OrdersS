from Models.Base import *
class Statuses(Base):
    id = PrimaryKeyField
    status_name = CharField()
    class Meta:
        table_name = 'statuses'

if __name__ == "__main__":
    pass