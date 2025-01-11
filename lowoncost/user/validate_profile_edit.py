from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Length

# validate add and edit deal form
class edit_profile(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Deal name is required."),
            Length(min=3, max=150, message="Deal name must be between 3 and 150 characters.")
        ]
    )
    
    description = TextAreaField(
        'Bio',
        validators=[
            DataRequired(message="Product link is required."),
            Length(min=6, max=500, message="Description must be more than 6 and less than 500 characters.") 
        ]
    )
    