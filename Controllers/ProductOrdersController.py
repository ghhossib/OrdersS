from Models.Products_Orders import *


class ProductOrdersController:
    # метод вывода всех записей таблицы статусы

    @classmethod
    def show(cls, id):
        return Products_Orders.get_or_none(id)

    @classmethod
    def add(cls, order_id,product_id):
        Products_Orders.create(order_id=order_id,product_id=product_id )

    @classmethod
    def get(cls):
        return Products_Orders.select()

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Products_Orders.update({key: value}).where(Products_Orders.id == id).execute()

    @classmethod
    def delete(cls, id):
        Products_Orders.delete_by_id(id)


if __name__ == "__main__":
    for row in ProductOrdersController.get():
        print(row.id, row.order_id, row.product_id)
    print(ProductOrdersController.show(11))




