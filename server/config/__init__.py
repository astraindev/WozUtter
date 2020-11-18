"""Config"""

from os import environ
from os.path import dirname, basename, isfile
import glob

modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


class Config(object):
    """
    The configuration class for Flask.

    The variables are set via the OS's environment variables:

    - SECRET_KEY - a sane default but really needs to be changed per
                   environment
    - DATABASE_URL - default is to use SQLite3

    The defaults are sane but probably need to be changed, especially if
    running on IBM Cloud's DB2 database.
    """
    SECRET_KEY = environ.get('SECRET_KEY', 'abc012def345ghi678jkl9AB')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///../wozutter.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_USE_SSL = bool(environ.get('RECAPTCHA_USE_SSL', False))
    RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = environ.get('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_OPTIONS = {}
