from Models.Base import *
class Statuses(Base):
    id = PrimaryKeyField
    status_name = CharField()

if __name__ == "__main__":
    connect().create_tables([Statuses])