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
            text  = item.get('text')
            author = item.get('author')
            category = item.get('tag')
            
            image_url = get_pexels_image(category)
        
            quoteOBJ = Quote(text=text, author= author, tag=category, image_url=image_url)
            
            print(f'{text} {author} {category}')
        
            return quoteOBJ
        
        
def get_pexels_image(category):
    request_url = pixelbay_api_url.format(pixelbay_api_key, category)
    
    with urllib.request.urlopen(request_url) as url:
        api_response = url.read()
        photo_obj = json.loads(api_response)
        
        return photo_obj['hits'][0]['webformatURL']