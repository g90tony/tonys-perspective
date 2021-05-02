import urllib.request, json
from .models import Article

def configure_request(app):
    globals quotes_url, pexels_api_key, pexels_url
    
    quotes_url = app.config['QUOTES_API_URL']
    pexels_api_key = app.config['PEXELS_API_KEY']
    pexels_url = app.config['PEXELS_URL']


def get_quote_of_the_day():
        
    with urllib.request.urlopen(quotes_url) as url:
        
        api_response = url.read()
        
        quote_json = json.loads(api_response)
        
        quote_data = quote_json.content.quotes[0]
        
        quoteOBJ = dict()
        
        quoteOBJ['quote']  = quote_data.quote
        quoteOBJ['author'] =quotes_data.author
        quoteOBJ['image_url'] = quote_data.background
        
        return quoteOBJ
        
    

