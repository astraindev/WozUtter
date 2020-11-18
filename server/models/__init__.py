"""Models"""

import glob
from os.path import dirname, basename, isfile

from server import login
from server.models.wozuser import WozUser

modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


@login.user_loader
def load_user(id: str) -> WozUser:
    """
    Stores the given user into the current user's session, which allows for
    easy retrieval of the instantiated user object.

    :param id: the ID of the user
    :return: the instantiated TaskyUser
    """
    return WozUser.query.get(int(id))
