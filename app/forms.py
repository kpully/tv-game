from flask_wtf import Form
from wtforms import StringField, PasswordField, RadioField, BooleanField, IntegerField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, Required

class MyForm(Form):
    name = StringField('First Name', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[Required()])
    time = SelectField('Time', choices=[('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3')])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    alc = SelectField('Alcohol', choices=[('0.12', 'White Wine'), ('0.13', 'Red Wine'), ('0.4', 'Vodka'), ('0.12', 'Champagne'), ('0.4', 'Whiskey'), ('0.04', 'Beer')], validators=[DataRequired()])
    drunk = SelectField('How drunk do you want to be?', choices=[('0.05', 'Buzzed'), ('0.1', 'Tipsy'), ('0.18', 'Hammered'), ('0.3', 'Blackout')], validators=[DataRequired()])
    submit = SubmitField('Submit')


class OlympicForm(Form):
    name = StringField('First Name', validators=[DataRequired()])
    weight = PasswordField('Weight', validators=[Required(), Regexp('^[0-9]$', 0, 'Weights must only have numbers')])
    time = SelectField('Time', choices=[('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3')])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    alc = SelectField('Alcohol', choices=[('0.12', 'White Wine'), ('0.13', 'Red Wine'), ('0.4', 'Vodka'), ('0.12', 'Champagne'), ('0.4', 'Whiskey'), ('0.04', 'Beer')], validators=[DataRequired()])
    submit = SubmitField('Submit')
	#sports = SelectMultipleField('Which events are you watching?', choices=[('general', 'Whatevers on'), ('swimming', 'Swimming'), ('gymnastics_women', 'Womens Gymnastics'), ('gymnastics_men', 'Mens Gymnastics'), ('track', 'Track'), ('basketball', 'Basketball'), ('field_hockey', 'Field Hockey'), ('fencing', 'Fencing')])