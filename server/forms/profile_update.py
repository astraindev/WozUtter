from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ProfileUpdateForm(FlaskForm):
    """
    The Flask form to update the user in the WozUser database.
    """
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Update')
