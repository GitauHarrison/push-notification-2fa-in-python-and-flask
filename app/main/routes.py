from app.main import bp
from flask import render_template
from flask_login import login_required


@bp.route('/')
@bp.route('/home')
@login_required
def home():
    return render_template('home.html',
                           title='Home'
                           )
