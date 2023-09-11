import os

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///project.db"
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # G spots
    from . import auth, views
    from app.models import db

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Views
    app.register_blueprint(auth.bp)
    app.register_blueprint(views.bp)

    app.add_url_rule('/', endpoint='index')

    return app
