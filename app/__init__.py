import os

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'faskr.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # G spots
    from . import db, auth, views

    db.init_app(app)

    # Views
    app.register_blueprint(auth.bp)
    app.register_blueprint(views.bp)

    app.add_url_rule('/', endpoint='index')

    return app
