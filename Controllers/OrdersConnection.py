from Models.Orders import *



class OrdersController:
    # метод вывода всех записей таблицы статусы

    @classmethod
    def show(cls, id):
        return Orders.get_or_none(id)

    @classmethod
    def add(cls, name, date,status_id, client_id, product_id,payment_id,description,delivery_data,delivery_payment):
        Orders.create(name=name,
                      date=date,
                      status_id=status_id,
                      client_id=client_id,
                      product_id=product_id,
                      payment_id=payment_id,
                      description=description,
                      delivery_data=delivery_data,
                      delivery_payment=delivery_payment)


    @classmethod
    def report(cls):
        pass

    @classmethod
    def get(cls):
        return Orders.select()

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Orders.update({key: value}).where(Orders.id == id).execute()

    @classmethod
    def delete(cls, id):
        Orders.delete_by_id(id)


if __name__ == "__main__":
    OrdersController.add('zakaz','2025-02-02','2','35','3','3','asdasdas','sssss','asdasdas')



