from flask_wtf import RecaptchaField
from server.forms.signup import SignupForm


class SignupRecaptchaForm(SignupForm):
    """
    Adds Google reCAPTCHA v2 functionality to the sign up form.
    """
    recaptcha = RecaptchaField()
