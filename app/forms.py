

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length

from app.models import User
from wtforms.validators import ValidationError,Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

def __init__(self, username, password):
    self.username = username
    self.password = password

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=8, max=16)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #name = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirmpassword = PasswordField('Repeat Password', validators=[DataRequired(),EqualTo('password')])
    #lastname = StringField('Lastname', validators=[DataRequired()])
    #phonenumber = IntegerField('Phonenumber', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        user= User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use different email address')

def __init__(self, username, email, password, confirmpassword):
    self.username = username
    self.email = email
    self.password = password
    self.confirmpassword = confirmpassword
    


#class Search(FlaskForm):
    #search= 