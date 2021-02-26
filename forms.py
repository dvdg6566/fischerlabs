from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, SelectField, SubmitField, TextAreaField, validators

class SearchCompoundForm(FlaskForm):
    compound = TextAreaField('Code Goes Here')
    submit = SubmitField('Submit Code')