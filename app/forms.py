from flask_wtf import Form
from wtforms import StringField, PasswordField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email

class MyForm(Form):
    name = StringField('FirstName', validators=[DataRequired()])
    weight = PasswordField('Weight', validators=[DataRequired()])
    gender = RadioField('Gender', validators=[DataRequired()])
    alc = BooleanField('Alcohol', validators=[DataRequired()])