from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, EqualTo
from email_validator import validate_email, EmailNotValidError

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), length(min = 3 , max=100)])
    email = StringField('email', validators=[DataRequired()])
    try:
  # Validate.
       valid = validate_email(" @ ")
       email = valid.email
    except EmailNotValidError as e:
       print(str(e))

  
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')


class LoginForm(FlaskForm):
   
    email = StringField('email', validators=[DataRequired()] )
     
    try:
  # Validate.
       valid = validate_email(" @ ")
       email = valid.email
    except EmailNotValidError as e:
       print(str(e))
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('login')