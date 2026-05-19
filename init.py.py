from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)
    
    # Configuration de Talisman pour les en-têtes de sécurité
    csp = {
        'default-src': ["'self'"],
        'script-src': ["'self'", "'unsafe-inline'"],
        'style-src': ["'self'", "'unsafe-inline'"]
    }
    Talisman(app, content_security_policy=csp)
    
    # Configuration CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    return app
