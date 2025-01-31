from wtforms import Form, StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
from email_validator import validate_email, EmailNotValidError
import dns.resolver
# from wtforms.fields import html5
# from wtforms.widgets import html5 as h5w

def is_valid_email(email):
    try:
        # Validate email format
        valid = validate_email(email, check_deliverability=False)
        domain = valid.domain

        # Check if domain has MX records
        return bool(dns.resolver.resolve(domain, 'MX'))
    
    except (EmailNotValidError, dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False



class SignupForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Username is required."),
            Length(min=3, max=20, message="Username must be between 3 and 20 characters."),
            Regexp('^[a-zA-Z0-9]*$', message="Username must not contain special characters.")
        ]
    )
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Email is required."),
            Length(min=3, max=50, message="Email must be between 3 and 30 characters."),
            Email(message="Invalid email address.")
        ]
    )
    
    
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="Password is required."),
            Length(min=6, max=20, message="Password must be more than 6 and less than 20 characters.")
        ]
    )
    confirm_password = PasswordField(
        'Confirm-Password',
        validators=[
            DataRequired(message="Please confirm your password."),
            EqualTo('password', message="Confirm Passwords must match."),
            Length(min=6, max=20, message="Password must be more than 6 and less than 20 characters.")
        ]
    )



class LoginForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Username is required."),
            Length(min=3, max=20, message="Username must be between 3 and 20 characters."),
            Regexp('^[a-zA-Z0-9]*$', message="Username must not contain special characters.")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="Password is required."),
            Length(min=6, max=20, message="Password must be more than 6 and less than 20 characters.")
        ]
    )


