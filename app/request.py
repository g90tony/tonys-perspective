import urllib.request, json
from .models import Article

def configure_request(app):
    global quotes_url, pexels_api_key, pexels_url
    
    quotes_url = app.config['QUOTES_URL']
    pexels_api_key = app.config['PEXELS_API_KEY']
    pexels_url = app.config['PEXELS_URL']


def get_quote_of_the_day():
        
    with urllib.request.urlopen(quotes_url) as url:
        
        api_response = url.read()
        
        quote_json = json.loads(api_response)
        
        quote_data = quote_json.quotes[0]
        
        quoteOBJ = dict()
        
        quoteOBJ['text']  = quote_data.quote
        quoteOBJ['author'] =quotes_data.author
        quoteOBJ['tag'] = quote_data.background
        
        return quoteOBJ
        
        
def get_pexels_image(category):
    url = pexels_url.format(category)
    headers = dict()
    
    headers['authorization'] = pexels_api_key 
    
    requestOBJ = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(requestOBJ) as url:
        api_response = url.read()
        photo_obj = json.loads(api_response)
        
        return photo_obj.photos.src.original