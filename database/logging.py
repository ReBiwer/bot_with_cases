from peewee import *


db = SqliteDatabase('database/loging_action.db')


class User(Model):
    username = CharField()
    action = CharField()
    time_action = DateField()

    class Meta:
        database = db


db.connect()
db.create_tables([User])
