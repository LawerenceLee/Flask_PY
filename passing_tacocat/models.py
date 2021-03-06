import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('taco.db', threadlocals=True)


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, email, password):
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=generate_password_hash(password))
        except IntegrityError:
            raise ValueError("User already exists")


class Taco(Model):
    user = ForeignKeyField(
        rel_model=User,
        related_name='tacos'
    )
    protein = CharField(default=None)
    cheese = BooleanField(default=False)
    shell = CharField(default="Flour")
    extras = TextField(default=None)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco], safe=True)
    DATABASE.close()