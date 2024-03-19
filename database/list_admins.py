from peewee import *


db = SqliteDatabase('database/list_admins.db')


class Admin(Model):
    id_admin = IntegerField()
    username_admin = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Admin])
