from app import app, db
from app.models import User, Item
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    usertype = SelectField('User Type', choices=[('Vendor', 'Vendor'), ('Customer', 'Customer')])
    remember = BooleanField('Remember Me')
    submit   = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    usertype = SelectField('User Type', choices=[('Vendor', 'Vendor'), ('Customer', 'Customer')])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Verify Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('That username is taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('An account using that email already exists.')


''' 
INCOMPLETE

class ProductSearchForm(Form):
    select = SelectField('Search among:', choices=[('vendors', 'Vendors'), ('products', 'Products')])
    search = StringField('')
'''