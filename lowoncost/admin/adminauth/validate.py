from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp
# from wtforms.fields import html5
# from wtforms.widgets import html5 as h5w


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
