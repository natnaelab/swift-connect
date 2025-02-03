from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class OnboardingForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    swift_code = StringField('SWIFT Code', validators=[Length(min=8, max=11)])
    submit = SubmitField('Submit Request') 