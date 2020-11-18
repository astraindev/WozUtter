from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from server.models.wozuser import WozUser


class SignupForm(FlaskForm):
    """
    The sign up Flask form to add the user to the WozUser database.
    """
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')

    def validate_username(self, username: str):
        """
        Makes sure that the chosen username doesn't already exist in the
        Tasky database.

        :param username: the username imputed from the form
        :return: None
        :raises: a validation error if the username is not unique
        """
        user = WozUser.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
