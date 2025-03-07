from datetime import datetime, timedelta
from itertools import count

from Models.Orders import *



class OrdersController:
    # метод вывода всех записей таблицы статусы

    @classmethod
    def show(cls, id):
        return Orders.get_or_none(id)

    @classmethod
    def add(cls, name, date,client_id,description,status_id=3,payment_id=None,delivery_data=2):
        if payment_id is not None:
            status_id = 2
        Orders.create(name=name,
                      date=date,
                      status_id=status_id,
                      client_id=client_id,
                      payment_id=payment_id,
                      description=description,
                      delivery_data=delivery_data,)


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
    def report_month(cls, start_date):
        # Преобразуем start_date в объект datetime
        start_date = datetime.strptime(start_date, '%Y-%m-%d')

        # Определяем первый день следующего месяца
        if start_date.month == 12:
            next_month = start_date.replace(year=start_date.year + 1, month=1, day=1)
        else:
            next_month = start_date.replace(month=start_date.month + 1, day=1)

        # Последний день текущего месяца — это день перед первым днём следующего месяца
        end_date = next_month - timedelta(days=1)

        # Выполняем запрос
        count = Orders.select().where(
            (Orders.date >= start_date) & (Orders.date <= end_date)
        ).count()

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
    OrdersController.add('zakaz','2023-10-16','2','asdas',payment_id=3,)
    #OrdersController.report_day('2023-10-16')
    #OrdersController.report_month('2023-10-01', '2023-10-31')
    #print(OrdersController.report_day('2022-03-15'))
    # for row in OrdersController.get():
    #     print(row.id, row.name,row.date,row.status_id,row.client_id,row.delivery_payment,row.payment_id,row.description,row.delivery_data)
    # print(OrdersController.show(4))
    #print(OrdersController.report_month('2023-09-10'))




