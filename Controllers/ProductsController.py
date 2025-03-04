from Models.Products import *


class ProductsController:
    # метод вывода всех записей таблицы статусы

    @classmethod
    def show(cls, id):
        return Products.get_or_none(id)
    @classmethod
    def add(cls, name, price, count, description):
        Products.create(name=name, price=price, count=count, description=description)

    @classmethod
    def get(cls):
        return Products.select()
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Products.update({key: value}).where(Products.id == id).execute()

    @classmethod
    def delete(cls,id):
        Products.delete_by_id(id)


if __name__ == "__main__":
    for row in ProductsController.get():
        print(row.id, row.name, row.price, row.count, row.description)
    print(ProductsController.show(11))
    


