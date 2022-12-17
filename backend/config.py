class Config:
    """
    This class holds configuration options for the Flask app.
    """
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/main'
    SQLALCHEMY_TRACK_MODIFICATIONS = False