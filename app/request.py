import urllib.request, json
from .models import Article, Quote

def configure_request(app):
    global quotes_url, pixelbay_api_key, pixelbay_api_url
    
    quotes_url = app.config['QUOTES_URL']
    pixelbay_api_key = app.config['PIXELBAY_API_KEY']
    pixelbay_api_url = app.config['PIXELBAY_API_URL']
    


def get_quote_of_the_day():
        
    with urllib.request.urlopen(quotes_url) as url:
        
        api_response = url.read()
        
        quote_json = json.loads(api_response)
        
        quote_data = quote_json['quotes']
        
        quoteOBJ = dict()
        for item in quote_data:
            quoteOBJ['text']  = item.get('text')
            quoteOBJ['author'] = item.get('author')
            quoteOBJ['category'] = item.get('tag')
            
            image_res = get_pexels_image(item.get('tag'))
           
           
            quoteOBJ['image_url'] = image_res 
            print(image_res)
    
        
            return quoteOBJ
        
        
def get_pexels_image(category):
    request_url = pixelbay_api_url.format(pixelbay_api_key, category)
    
    with urllib.request.urlopen(request_url) as url:
        api_response = url.read()
        photo_obj = json.loads(api_response)
        
        return photo_obj['hits'][0]['webformatURL']