from flask import Flask

from app.extensions import db, jwt


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    jwt.init_app(app)

    from app.auth.routes import auth
    from app.tasks.routes import tasks
    from app.users.routes import users

    app.register_blueprint(auth, url_prefix="/api/auth")
    app.register_blueprint(tasks, url_prefix="/api/tasks")
    app.register_blueprint(users, url_prefix="/api/users")

    with app.app_context():
        db.create_all()
    @app.route("/")
    def home():
     return "Week 9 Task Management REST API is Running!"
    return app