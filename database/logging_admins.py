from peewee import *

db = SqliteDatabase('database/log_action.db')


class AdminAction(Model):
    id_admin = IntegerField()
    username_admin = CharField()
    action_admin = CharField()
    time_action = DateTimeField(formats='%Y-%m-%d %H:%M:%S')

    class Meta:
        database = db


db.connect()
db.create_tables([AdminAction])