from Models.Base import *
class Payment(Base):
    id = PrimaryKeyField()
    data = DateTimeField()
    summ = DecimalField()
    class Meta:
        table_name = 'payment'

if __name__ == "__main__":
   pass