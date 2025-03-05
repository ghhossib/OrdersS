from Models.Base import *
from Models.Orders import Orders
from Models.Products import Products


class Products_Orders(Base):
    id = PrimaryKeyField
    order_id = ForeignKeyField(Orders)
    product_id = ForeignKeyField(Products)
    class Meta:
        table_name = 'products_orders'

if __name__ == "__main__":
    pass