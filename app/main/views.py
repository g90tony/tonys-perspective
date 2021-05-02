from flask import render_template, url_for, redirect
from flask_login import current_user, login_required

from . import main
from .forms import LoadMoreArticles, AddComment
from .. import db, photos
from ..models import Article, Category, Comment, User, Quote
from ..request import get_quote_of_the_day, get_pexels_image

def get_article_category_title(articles):
    final_list = list()
    for article in articles:
        temp = article
        
        article_category = Category.get_category(temp.category)
        
        temp["category"] = article_category.title
        final_list.append(temp)

@main.route('/', methods=['GET, POST'])
def index():
    title: "Welcome to Tony's Perspective"
    
    popular_articles = Article.get_popular()
    recent_articles = Article.get_recent()
    
    qotd = get_quote_of_the_day()
    quote_img = get_pexels_image(qotd.tag)
    
    new_quote = Quote(text= qotd.text, author= qotd.author, tag= qotd.tag, image_url= quote_img)
    
    form = LoadMoreArticles()
    current_page = 1
    
    if form.validate_on_submit():
        current_page = current_page + 1
        more_recent_articles = Article.get_more_recent(current_page)
            
    if popular_list:
       popular_list = get_article_category_title(popular_articles)

    if recent_posts:
      recent_list = get_article_category_title(recent_articles)
            
    if more_recent_articles:
        recent_list = get_article_category_title(more_recent_articles)
        
        
    return render_template('pages/landing.html', popular = popular_list, recent = recent_list, quote = new_quote, title=title)
        
     
