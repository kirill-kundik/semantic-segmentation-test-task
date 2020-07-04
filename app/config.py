from os import environ


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    FLASK_APP = environ.get('FLASK_APP', 'app')
    FLASK_ENV = environ.get('FLASK_ENV', 'development')
