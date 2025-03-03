from Models.Base import *
class Payment(Base):
    id = PrimaryKeyField()
    data = DateTimeField()
    summ = FloatField()

if __name__ == "__main__":
    connect().create_tables([Payment])