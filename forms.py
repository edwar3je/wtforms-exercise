from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """A template for a form that is used to collect information to create a new pet instance for the 'pets' table in the database.
    Only two of the fields are required, but if any of the optional fields are left blank, default values will be assigned to the 
    pet instance."""
    name = StringField("Pet Name *", validators=[InputRequired(message="Please provide a name")])
    species = SelectField("Species *", choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL (optional)", validators=[Optional(), URL(require_tld=False, message="Please provide a valid url for the photo")])
    age = IntegerField("Age (optional)", validators=[Optional(), NumberRange(min=0, max=30, message="Please provide a number that is between 0 and 30")])
    notes = StringField("Notes (optional)", validators=[Optional()])

class EditPetForm(FlaskForm):
    """A template for a form that is used to collect information to edit a specific pet instance for the 'pets' table in the database
    (but only if "new" information is provided)"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=False, message="Please provide a valid url for the photo")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available", default="checked")