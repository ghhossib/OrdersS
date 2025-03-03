from Models.Base import *
class Products(Base):
    id = PrimaryKeyField
    name = CharField()
    price = DecimalField()
    count = IntegerField()
    description = TextField()

if __name__ == "__main__":
    connect().create_tables([Products])