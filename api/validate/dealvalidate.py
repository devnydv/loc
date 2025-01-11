from wtforms import Form, StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


#not in use may be used letter
class adddeal(Form):
    title = StringField(
        'title',
        validators=[
            DataRequired(message="Deal name is required."),
            Length(min=3, max=150, message="Deal name must be between 3 and 150 characters.")
        ]
    )
    imageUrl = PasswordField(
        'imgUrl',
        validators=[
            DataRequired(message="Image is required."),
            Length(min=6, max=200, message="Image URl must be more than 6 and less than 200 characters.")
        ]
    )
    dealUrl = StringField(
        'dealUrl',
        validators=[
            DataRequired(message="Product link is required."),
            Length(min=6, max=200, message="Deals URl must be more than 6 and less than 200 characters.") 
        ]
    )
    description = StringField(
        'description',
        validators=[
            DataRequired(message="Product link is required."),
            Length(min=6, max=500, message="Description must be more than 6 and less than 500 characters.") 
        ]
    )
    currentPrice = StringField(
        'currentPrice ',
        validators=[
            DataRequired(message="Current price is required."),
            # Length(min=1, max=9, message="Price must be more than 0 and less than 999999999.")
        ]
    )
    originalPrice = StringField(
        'originalPrice',
        validators=[
            DataRequired(message="Original price is required."),
            # Length(min=1, max=9, message="Price must be more than 0 and less than 999999999.") 
        ]
    )