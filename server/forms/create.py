from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
    """
    A Flask form to add new posts
    """
    message = StringField('Post', validators=[DataRequired()])
    submit = SubmitField('Add')
