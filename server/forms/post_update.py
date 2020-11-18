from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostUpdateForm(FlaskForm):
    """
    A Flask form to update posts
    """
    message = StringField('Post', validators=[DataRequired()])
    submit = SubmitField('Update')
