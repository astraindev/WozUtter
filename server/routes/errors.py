from flask import render_template

from server import app


@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return render_template('404.html', title='Not Found')
