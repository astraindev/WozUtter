from server import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class WozUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', cascade="all,delete", backref='woz_user', lazy='dynamic')

    def __repr__(self) -> str:
        """
        Method to display sane text for the WozUser.

        :return: a string showing the print() and repr() text
        """
        return '<WozUser {}>'.format(self.username)

    def set_password(self, password: str):
        """
        The setter method to store the user's hashed password.

        :param password: the plain text of the user's password
        :return: None
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        The getter (is) method to see if the user's password is correct.

        :param password:
        :return: True of the password match succeeds, otherwise False
        """
        return check_password_hash(self.password_hash, password)
