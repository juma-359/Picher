from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])

    username = StringField('Enter your username',validators=[Required()])

    password = PasswordField('Password',validator=[Required()])

    confirm_password = PasswordField('Confirm Passwords',validators = [required()])

    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [Required(), Email()])

    password = PasswordField('Password', validators = [Required()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Log in')