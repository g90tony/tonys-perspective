from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_required

from . import main
from .forms import LoadMoreArticles, AddComment
from .. import db, photos
from ..models import Article, Category, Comment, User, Quote
from ..request import get_quote_of_the_day, get_pexels_image

def get_article_category_title(articles):
    final_list = list()
    
    for article in articles:
        temp = dict()
        category = Category.query.filter_by(id = article.category).first()
        temp['id'] = article.id 
        temp['image_url'] = article.image_url
        temp['title'] = article.title
        temp['date'] = article.date
        temp['content'] = article.content
        temp['views'] = article.views
        temp['comments'] = article.comments
        temp['category'] = category.title     

        final_list.append(temp)
        
    return final_list

@main.route('/', methods=['GET', 'POST'])
def index():
    title = "Welcome to Tony's Perspective"
    
    popular_articles = Article.get_popular()
    recent_articles = Article.get_recent()
        
    qotd = get_quote_of_the_day()
    
    form = LoadMoreArticles()
    current_page = 1
    
    if form.validate_on_submit():
        current_page == current_page + 1
        more_recent_articles = Article.get_more_recent(current_page)
  
        if more_recent_articles:
            recent_list = get_article_category_title(more_recent_articles)
            
            
    if popular_articles:
           popular_list = get_article_category_title(popular_articles)

    if recent_articles:
          recent_list = get_article_category_title(recent_articles)
                   
        
    return render_template('pages/landing.html', popular = popular_list, recent = recent_list, quote = qotd, form = form, title=title, user = current_user.is_authenticated)
        
     
@main.route('/articles/<category>')
def article_category(category, methods={'GET, POST'}):
    
    current_page = 1
    
    article_category = Category.get_category(category)
    
    title = f"Tony's Perspective: {article_category.title}"
    
    category_articles = Article.get_category(category)
    
    if category_articles:
        articles_list = get_article_category_title(category_articles)
        
        
    form = LoadMoreArticles()
    
    if form.validte_on_submit():
        current_page = current_page + 1
        more_category_articles = Article.get_more_recent(current_page)
        
    articles_list = get_article_category_title(more_category_articles)
        
        
    return render_template('pages/category.html', category_title= article_category.title, category_posts= articles_list, title= title, user = current_user.is_authenticated)


@main.route('/articles/view/<int:article_id>')
def view_articles(article_id):
    
    article_data = Article.query.filter_by(id=article_id).first()
    
    related_articles = Article.query.filter_by(category = article_data.category).limit(5)
    
    if related_articles:
        related_list = get_article_category_title(related_articles)
    
    title = f"Tony's Perspective: {article_data.title}"
    
    if article_data:
        category_data = Category.get_category(article_data.category)
        
        article_item = dict()
        category = Category.query.filter_by(id = article_data.category).first()
        article_item['id'] = article_data.id 
        article_item['image_url'] = article_data.image_url
        article_item['title'] = article_data.title
        article_item['date'] = article_data.date
        article_item['content'] = article_data.content
        article_item['views'] = article_data.views
        article_item['comments'] = article_data.comments
        article_item['category'] = category_data.title   
            
    form = AddComment()
    if current_user.is_authenticated:
        
        if form.validte_on_submit():
            new_comment = form.comment_input.data
            
            user_comment = Comment(user_id = current_user.id, article_id = article_id, content = new_comment)
            
            user_comment.add_comment()        
    
    return render_template('pages/article.html', article = article_item, related = related_list, form = form, title = title, user = current_user.is_authenticated)
        

@login_required
@main.route('/articles/view/<int:article_id>/add-comment', methods=['POST'])
def add_comment(article_id):
          
    form = AddComment()
    
    if form.validate_on_submit() and current_user.is_authenticated:
        new_comment = form.comment_input.data
        
        user_comment = Comment(user_id = current_user.id, article_id = article_id, content = new_comment)
        
        user_comment.add_comment()
        
    else:
        flash('Please login to post a comment')
    return redirect(url_for('main.view_articles', article_id = article_id))