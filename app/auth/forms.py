
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please Enter A Valid Username")])
    password = PasswordField('Password', validators=[DataRequired(message="Please Enter A Valid Password")])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please Create And Enter A Username")])
    email = StringField('Email',
                        validators=[DataRequired(message="Please Enter An Email Address"),
                                    Email("Please Enter A Valid Email Address")])
    password = PasswordField('Password', validators=[DataRequired("Please Enter A Secure Password")])
    confirm = PasswordField(
        'Confirm Password',
        validators=[DataRequired("Please Confirm Password"), EqualTo('password', message="Passwords must match")])
    accept_tos = BooleanField('I Accept The Terms Of Service',
                              validators=[DataRequired("You Must Accept The Terms Of Service")])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different email Address.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')



