from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_sslify import SSLify
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from decouple import UndefinedValueError
from datetime import datetime
from oauthlib.oauth2 import WebApplicationClient
import stripe

import sys


# Initialize the Flask extensions without attaching them to the app
mail = Mail()
db = SQLAlchemy()
bc = Bcrypt()
lm = LoginManager()
csrf = CSRFProtect()


def create_app(config_class="app.config.Config", test_config=False):
    """Application factory to create a Flask application instance
    with the specified configuration.

    Args:
        config_class (str): Reference to the configuration object to use.
        test_config (bool): If True, apply the test configuration.
    Returns:
        app (Flask): The Flask application instance.
    """

    # Initialize the flask app
    app = Flask(__name__)

    # Load the Config object
    try:
        app.config.from_object(config_class)
    except UndefinedValueError as e:
        print(
            "Please make sure you have all the required environment variables set.", e
        )
        sys.exit()

    # If specified, load the test configuration to override the Config object
    if test_config:
        # Disable Postgres pooling when SQLite is used
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}

    # Initialize the Flask extensions for the app instance
    mail.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    bc.init_app(app)
    lm.init_app(app)
    csrf.init_app(app)
    SSLify(app)

    # Enable CORS for all routes
    CORS(
        app,
        resources={r"/*": {"origins": [app.config["APP_ROOT_URL"]]}},
        supports_credentials=False,
    )

    # Set up the database tables if they don't exist
    try:
        with app.app_context():
            # Import the table models
            from app.models import Users, Tiers

            # Create the database tables if they don't exist
            db.create_all()

            # If there are no tiers in the database, create the default tiers
            if Tiers.query.count() == 0:
                default_tier = Tiers(name="free", label="Free")
                db.session.add(default_tier)
                db.session.commit()
                print(" * Default tiers created successfully.")

    except Exception as e:
        print("Error creating the database tables.")
        print(e)
        sys.exit()

    # Import the Blueprints
    from app.views import public_bp
    from app.views_private import private_bp
    from app.views_auth import auth_bp

    # Register the Blueprints
    app.register_blueprint(public_bp, url_prefix="/")
    app.register_blueprint(private_bp, url_prefix="/app")
    app.register_blueprint(auth_bp, url_prefix="/")

    # Variables available in all templates
    @app.context_processor
    def inject_globals():
        return {
            "APP_NAME": app.config["APP_NAME"],
            "COPYRIGHT": f"2021–{datetime.now().year} - {app.config['APP_NAME']}",
        }

    # Redirect pages with trailing slashes to versions without
    # Applies to other Blueprints like app_private as well
    @app.before_request
    def remove_trailing_slash():
        if (
            request.path != "/"
            and request.path != "/app/"
            and request.path.endswith("/")
        ):
            return redirect(request.path[:-1])

    # Register a Jinja2 filter for date formatting
    @app.template_filter("dateformat")
    def dateformat_filter(value, format="%B %d, %Y"):
        return datetime.fromtimestamp(value).strftime(format)

    # Register a Jinja2 filter for time formatting
    @app.template_filter("timeformat")
    def timeformat_filter(value, format="%I:%M %p"):
        return datetime.fromtimestamp(value).strftime(format)

    # Google OAuth 2 client configuration
    app.google_client = WebApplicationClient(app.config["GOOGLE_CLIENT_ID"])

    # Stripe setup
    stripe.api_key = app.config["STRIPE_SECRET_KEY"]

    # Return the app instance created
    return app
