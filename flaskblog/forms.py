from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, EqualTo, ValidationError
from email_validator import validate_email, EmailNotValidError
from flaskblog.models import User

#Registration form inputs

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), length(min = 3 , max=100)])
    email = StringField('email', validators=[DataRequired()])

    # Validate email.

    try:
       valid = validate_email(" @ ")
       email = valid.email
    except EmailNotValidError as e:
       pass

  
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')

#vaidate username

    def validate_username(self, username):
       user = User.query.filter_by(username=username.data).first()
       if user:
          raise ValidationError('That username is already taken. Please use another username')

#validate email

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
           raise ValidationError('That email is already taken. Please use another email')

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