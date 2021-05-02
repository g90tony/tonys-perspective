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
        
     
@main.route('/articles/<category>')
def article_category(category, methods={'GET, POST'}):
    
    current_page = 1
    
    article_category = Category.get_category(category)
    
    title = f"Tony's Perspective: {article_category.title}"
    
    category_articles = Article.get_category(category)
    
    if category_articles:
        articles_list = get_article_category_title(category_articles)
        
        
    form = LoadMoreArticles()
    
    if form.validate_on_submit():
        current_page = current_page + 1
        more_category_articles = Article.get_more_recent(current_page)
        
    articles_list = get_article_category_title(more_category_articles)
        
        
    return render_template('pages/category.html' category_title= article_category.title, category_posts= articles_list, title= title)


@main.route('/articles/view/<int:article_id>')
def view_articles(article_id):
    
    article_data = Article.get_article(article_id)
    
    title = f"Tony's Perspective: {article_data.title}"
    
    if article_data:
        category_data = Category.get_category(article_data.category)
        article_data[category] = category_data.title
        
    related_articles = Article.get_related_articles(category_data.id)
    
    if related_articles:
        related_list = get_article_category_title(related_articles)
        
    if current_user.is_authenticated:
        form = AddComment()
    
        if form.validate_on_submit():
            new_comment = form.comment_input.data
            
            user_comment = Comment(user_id = current_user.id, article_id= article_id, content = new_comment)
            
            user_comment.add_comment()
            
    else
        form = None
        
    
    return render_template()
        

@login_required
@main.route('/articles/view/<int:article_id>/add-comment', methods=['POST'])
def add_comment(article_id):
          
    form = AddComment()
    
    if form.validate_on_submit():
        new_comment = form.comment_input.data
        
        user_comment = Comment(user_id = current_user.id, article_id= article_id, content = new_comment)
        
        user_comment.add_comment()
        
        redirect(url_for('main.view_article', article_id = article_id))
    
    