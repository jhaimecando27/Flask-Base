from flask import Blueprint, render_template, session
from .auth import login_required

bp = Blueprint('views', __name__, url_prefix="/")


@bp.route('/')
@login_required
def index():
    """Home Page"""

    return render_template('app/index.html')
