import urllib.request, json
from .models import Article

def configure_request(app):
    globals quotes_url, pexels_api_key, pexels_url
    
    quotes_url = app.config['QUOTES_API_URL']
    pexels_api_key = app.config['PEXELS_API_KEY']
    pexels_url = app.config['PEXELS_URL']
'