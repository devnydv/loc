from wtforms import Form, StringField, TextAreaField, URLField, IntegerField
from wtforms.validators import DataRequired, Length, URL

# validate add and edit deal form
class adddeal(Form):
    title = StringField(
        'Deal Title',
        validators=[
            DataRequired(message="Deal name is required."),
            Length(min=3, max=150, message="Deal name must be between 3 and 150 characters.")
        ]
    )
    imageUrl = URLField(
        'Image URL',
        validators=[
            DataRequired(message="Image is required."),
            URL(message='Invalid URL'),
            Length(min=6, max=200, message="Image URl must be more than 6 and less than 200 characters.")
        ]
    )
    dealUrl = URLField(
        'Deals Url',
        validators=[
            DataRequired(message="Product link is required."),
            URL(message='Invalid URL'),
            Length(min=6, max=200, message="Deals URl must be more than 6 and less than 200 characters.") 
        ]
    )
    description = TextAreaField(
        'Description',
        validators=[
            DataRequired(message="Product link is required."),
            Length(min=100, max=1500, message="Description must be more than 100 and less than 1500 characters.") 
        ]
    )
    # pros = StringField(
    #     'Pros',
    #     validators=[
    #         Length(min=0, max=1000, message="Deal name must be between 0 and 1000 characters.")
    #     ]
    # )
    # cons = StringField(
    #     'Cons',
    #     validators=[ 
    #         Length(min=0, max=1000, message="Deal name must be between 0 and 1000 characters.")
    #     ]
    # )
    currentPrice = IntegerField(
        'Current Price',
        validators=[
            DataRequired(message="Current price is required."),
            # Length(min=1, max=9, message="Price must be more than 0 and less than 999999999.")
        ]
    )
    originalPrice = StringField(
        'Original Price',
        validators=[
            DataRequired(message="Original price is required."),
            # Length(min=1, max=9, message="Price must be more than 0 and less than 999999999.") 
        ]
    )