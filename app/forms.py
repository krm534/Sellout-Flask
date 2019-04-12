from app import app, db
from app.models import User, Item
from flask_wtf import FlaskForm
from flask import request
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, FormField, FieldList
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import phonenumbers


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    usertype = SelectField('User Type', choices=[('Vendor', 'Vendor'), ('Customer', 'Customer')])
    remember = BooleanField('Remember Me')
    submit   = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired()])
    email       = StringField('Email', validators=[DataRequired(), Email()])
    phone       = StringField('Phone Number', validators=[DataRequired()])
    firstname   = StringField('First Name', validators=[DataRequired()])
    lastname    = StringField('Last Name', validators=[DataRequired()])
    usertype    = SelectField('User Type', choices=[('Vendor', 'Vendor'), ('Customer', 'Customer')])
    password    = PasswordField('Password', validators=[DataRequired()])
    password2   = PasswordField(
        'Verify Password', validators=[DataRequired(), EqualTo('password')])
    
    submit      = SubmitField('Sign Up')

    #local field validators
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('That username is taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('An account using that email already exists.')

    def validate_phone(self, phone):
        try:
            number = phonenumbers.parse(phone.data, None)
            if not phonenumbers.is_possible_number(number):
                raise ValidationError('Invalid phone number.')

        except:
            number = phonenumbers.parse("+1"+phone.data, None)
            if not phonenumbers.is_possible_number(number):
                raise ValidationError('Invalid phone number.')

class AddToCartForm(FlaskForm):
    submit = SubmitField('Add to Cart')

class QuantityEntryForm(FlaskForm):
    quantity = IntegerField(validators=[DataRequired()])

    def validate_quantity(self, quantity):
        if quantity.data < 0:
            raise ValidationError('Invalid quantity.')

class CartQuantitiesForm(FlaskForm):
    quantities = FieldList(FormField(QuantityEntryForm), min_entries=1)
    submit = SubmitField('Done')


#elasticsearch form
class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)

