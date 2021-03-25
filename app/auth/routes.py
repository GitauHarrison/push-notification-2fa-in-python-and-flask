from app.auth import bp
from flask import render_template


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html',
                           title='Login'
                           )
