from Connection.Connect import *

class Base(Model):
    class Meta:
        database = connect()

    class Meta:
        table_name = 'Users'
