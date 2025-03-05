from datetime import datetime, timedelta
from itertools import count

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
        count = Orders.select().count()
        return count

    @classmethod
    def report_range(cls, day):
        given_day = datetime.strptime(day, '%Y-%m-%d')
        start_of_week = given_day - timedelta(days=given_day.weekday())
        week_days = [start_of_week + timedelta(days=i) for i in range(7)]
        count = Orders.select().where((Orders.date >= start_of_week) & (Orders.date <= week_days[6])).count()
        return count

    @classmethod
    def report_day(cls,day):
        return Orders.select().where(Orders.date == day).count()

    @classmethod
    def report_random(cls,day1,day2):
        return Orders.select().where(Orders.date.between(day1,day2)).count()

    @classmethod
    def report_month(cls, start_date,end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        count = Orders.select().where(
            (Orders.date>=start_date) & (Orders.date <= end_date)).count()
        return count


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
    #OrdersController.add('zakaz20','2023-10-19','2','35','3','3','asdasdas','sssss','asdasdas')
    OrdersController.report_day('2023-10-16')
    OrdersController.report_month('2023-10-01', '2023-10-31')
    # for row in OrdersController.get():
    #     print(row.id, row.name,row.date,row.status_id,row.client_id,row.product_id,row.delivery_payment,row.payment_id,row.description,row.delivery_data)
    # print(OrdersController.show(4))



