from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import (DataRequired, Regexp, ValidationError, 
                                Email, Length, EqualTo)

from models import User


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')


class RegisterForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class TacoForm(FlaskForm):
    protein = StringField("Protein:", validators=[DataRequired()])
    cheese = BooleanField("Would you like Cheese?", validators=None)
    shell = StringField("Shell Type:", validators=[DataRequired()])
    extras = TextAreaField("Any Extras?", validators=[DataRequired()])
