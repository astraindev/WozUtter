from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from server import app, db
from server.forms.login import LoginForm
from server.forms.delete import DeleteForm
from server.forms.profile_update import ProfileUpdateForm
from server.forms.signup import SignupForm
from server.forms.signup_recaptcha import SignupRecaptchaForm
from server.models.wozuser import WozUser


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/<int:user_id>')
@login_required
def read_user(user_id):
    user: WozUser = WozUser.query.filter_by(id=user_id).first()
    form_update: ProfileUpdateForm = ProfileUpdateForm()
    form_delete: DeleteForm = DeleteForm()
    return render_template('profile.html', title='Profile', user=user,
                           form_update=form_update, form_delete=form_delete)


@app.route('/users/<int:user_id>/update', methods=['POST'])
@login_required
def update_user(user_id):
    if current_user.id != user_id:
        return redirect(url_for('read_user'), user_id)

    form: ProfileUpdateForm = ProfileUpdateForm()
    user: WozUser = WozUser.query.filter_by(id=user_id).first()

    user.first_name = form.first_name.data
    user.last_name = form.last_name.data

    db.session.add(user)
    db.session.commit()
    flash('Profile updated')

    return redirect(url_for('read_user', user_id=user_id))


@app.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.id != user_id:
        return redirect(url_for('read_user'), user_id)

    user: WozUser = WozUser.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    flash('Profile removed')

    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    logs the user into WozUtter
    :return: the Login template
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user: WozUser = WozUser.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['POST'])
def logout():
    """
    Logs the user out of WozUtter redirecting to the login

    :return: a redirect to the login route
    """
    logout_user()
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Creates a new account for the user so that they can sign in.

    :return: initially, the Signup template then redirects to the login
             route after posting
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    recaptcha = app.config['RECAPTCHA_PRIVATE_KEY'] is not None
    if recaptcha:
        form = SignupRecaptchaForm()
    else:
        form = SignupForm()

    if form.validate_on_submit():
        user = WozUser()
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.username = form.username.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a new user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Signup', form=form, recaptcha=recaptcha)
