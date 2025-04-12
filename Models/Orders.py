from Models.Base import *
from Models.Payment import Payment
from Models.Products import Products
from Models.Statuses import Statuses
from Models.Users import Users


class Orders(Base):
    id = PrimaryKeyField
    name = CharField()
    date = DateTimeField()
    status_id = ForeignKeyField(Statuses)
    client_id = ForeignKeyField(Users)
    payment_id = ForeignKeyField(Payment)
    description = CharField()
    delivery_data = CharField()

    class Meta:
        table_name = 'orders'

if __name__ == "__main__":
    pass