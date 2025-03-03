from Models.Payment import *


class PaymentController:
    # метод вывода всех записей таблицы статусы
    @classmethod
    def get(cls):
        return Payment.select()

    @classmethod
    def show(cls, id):
        return Payment.get_or_none(id)

    @classmethod
    def add(cls, summ, data):
        Payment.create(summ=summ, data=data)

if __name__ == "__main__":
    for row in PaymentController.get():
        print(row.id, row.summ, row.data)
    print(PaymentController.show(11))
    PaymentController.add(4444, 12312444443)