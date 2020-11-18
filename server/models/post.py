from server import db


class Post(db.Model):
    """
    The model for the actual post. The user_id field is the foreign key
    for the user who created the post.
    """
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(140), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('woz_user.id'))

    def __repr__(self) -> str:
        """
        Method to display sane text for the Post.

        :return: a string showing the print() and repr() text
        """
        return '<Post {}>'.format(self.message)
