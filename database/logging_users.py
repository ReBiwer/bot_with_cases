from peewee import *


db = SqliteDatabase('database/log_action.db')


class UserAction(Model):
    id_user = IntegerField()
    username = CharField()
    action = CharField()
    time_action = DateTimeField(formats='%Y-%m-%d %H:%M:%S')

    class Meta:
        database = db


db.connect()
db.create_tables([UserAction])
