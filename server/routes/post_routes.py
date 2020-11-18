from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from server import app, db
from server.forms.create import CreateForm
from server.forms.delete import DeleteForm
from server.forms.post_update import PostUpdateForm
from server.models.post import Post

emojicons = {
    "=3": "😃",
    ":(": "☹️",
    ":'(": "😢",
    "D:": "😧",
    ":*": "😘",
    ";)": "😉",
    "0:)": "😇",
    "3:)": "😈",
    ":)": "🙂",
    "@}->--": "🌹",
    "<3": "❤️",
    "</3": "💔"
}


@app.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreateForm()

    if form.validate_on_submit():
        message: str = form.message.data

        for emojicon in emojicons:
            message = message.replace(emojicon, emojicons[emojicon])

        post: Post = Post()
        post.message = message
        post.user_id = current_user.id

        db.session.add(post)
        db.session.commit()

        flash('Your post has been, ummm ... well, posted. Duh!')
        return redirect(url_for('read_posts'))

    return render_template('create.html', title='New Message', form=form)


@app.route('/posts')
def read_posts():
    posts = Post.query.order_by(Post.id.asc())
    return render_template('posts.html', title='Posts', posts=posts)


@app.route('/posts/<int:post_id>')
def read_post(post_id):
    post: Post = Post.query.filter_by(id=post_id).first()
    form_update: PostUpdateForm = PostUpdateForm()
    form_delete: DeleteForm = DeleteForm()
    return render_template('post.html', title='Post', post=post, form_update=form_update, form_delete=form_delete)


@app.route('/posts/<int:post_id>/update', methods=['POST'])
def update_post(post_id):
    post: Post = Post.query.filter_by(id=post_id).first()

    if current_user.id == post.user_id:
        form: PostUpdateForm = PostUpdateForm()
        message: str = form.message.data

        for emojicon in emojicons:
            message = message.replace(emojicon, emojicons[emojicon])

        post.message = message;

        db.session.add(post)
        db.session.commit()
        flash('Post updated')

    return redirect(url_for('read_post', post_id=post_id))


@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post: Post = Post.query.filter_by(id=post_id).first()

    if current_user.id == post.user_id:
        db.session.delete(post)
        db.session.commit()
        flash('Post removed')

    return redirect(url_for('read_posts'))
