from flask_wtf import FlaskForm
from wtforms import SubmitField


class DeleteForm(FlaskForm):
    """
    The Flask form to delete the post from the WozUser database.
    """
    submit = SubmitField('Yes')
