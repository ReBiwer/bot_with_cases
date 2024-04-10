from peewee import *


db = SqliteDatabase('database/list_admins.db')


class Admins(Model):
    id_admin = IntegerField()
    id_chat_with_bot = IntegerField()
    username_admin = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Admins])
