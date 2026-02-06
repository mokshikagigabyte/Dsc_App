import logging
from flask import Flask
from extensions import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)

    db.init_app(app)

    from routes.auth import auth_bp
    from routes.challenge import challenge_bp
    from routes.profile import profile_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(challenge_bp)
    app.register_blueprint(profile_bp)

    with app.app_context():
        db.create_all()

    return app
app= create_app()

if __name__ == "__main__":
    app.run(debug=True)

