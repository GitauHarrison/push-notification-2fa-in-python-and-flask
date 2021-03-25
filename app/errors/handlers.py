from flask import render_template
from app.errors import bp
from app import db


@bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html',
                           title='Page Not Found',
                           ), 404


@bp.errorhandler(500)
def internal_error(error):
    db.session.roll_back()
    return render_template('errors/500.html',
                           title='Internal Error',
                           ), 500
