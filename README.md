# WozUtter
WozUtter is a simple, safe, and secure alternative to Twitter. While there is only one place to write your WozUtters, it should be easy to use on a topical web site.

This was originally a final Hands-On project for the Woz U class _Backend Foundations - Java_. It has been ported to Python so as to not post an answer to the project for students to copy.

## Getting Started
First, be sure that Python 3 is installed. If not, be sure and install it now.

Next, make a virtual environment for Python 3 (macOS/Linux/UNIX):

```shell script
python3 -m venv venv
```

On Windows 10:

```shell script
python -m venv venv
```

Invoke the virtual environment (macOS/Linux/UNIX):

```shell script
source venv/bin/activate
```

On Windows 10:

```shell script
venv\Scripts\activate.bat
```

Then install the packages needed to run WozUtter:

```shell script
python -m pip install -r requirements.txt
```

Copy the `dotenv-default` file to `.env` and change the `SECRET_KEY` variable to something unique for your WozUtter app.

Finally, run the local WozUtter server:

```shell script
flask run
```

## Other Things ...
### Other Databases
By default, WozUtter uses the SQLite3 database. Using another database is pretty easy. Do the following steps:

1. Install the SQLAlchemy version of your database driver.
2. In the `.env` file, set or change the environment variable `DATABASE_URL` to the new connection URL.

### Google reCAPTCHA v2
WozUtter supports using a reCHAPCHA on the signup page. Follow these steps to set it up:

1. Sign up for the [Google reCAPTCHA v2](http://www.google.com/recaptcha/admin).
2. Copy the contents of the `dotenv-recaptcha` file and paste them into the `.env` file.
3. Change the `RECAPTCHA_PUBLIC_KEY` variable to your public key.
4. Change the `RECAPTCHA_PRIVATE_KEY` variable to your private key.
5. If you want to use SSL, change the `RECAPTCHA_USE_SSL` variable to True.

### WSGI
WozUtter supports WSGI deployment by providing a `wsgi.py` file. A `server-dist.ini` file is provided for uWSGI. Just copy it over as `server.ini` and modify, if need be.
