from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, SelectField, SubmitField, TextAreaField, validators

class SearchCompoundForm(FlaskForm):
    compound = TextAreaField('Code Goes Here')
    submit = SubmitField('Search')

class LoginForm(FlaskForm):
	username = TextAreaField('Username')
	password = TextAreaField('Password')
	submit = SubmitField('Sign In')
	newAccount = SubmitField('Sign up')

class SignupForm(FlaskForm):
	username = TextAreaField('Username')
	password = TextAreaField('Password')
	submit = SubmitField('Sign Up')

class Order(FlaskForm):
	submit = SubmitField('Submit Code')