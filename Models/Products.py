from Models.Base import *
class Products(Base):
    id = PrimaryKeyField
    name = CharField()
    price = DecimalField()
    count = IntegerField()
    description = TextField()
    class Meta:
        table_name = 'products'

if __name__ == "__main__":
  pass