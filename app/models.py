from flask_login import UserMixin
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy import text

from . import db
from . import login_manager

class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key = True)
    image_url = db.Column(db.String)
    title = db.Column(db.String)
    date = db.Column(db.String)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    content = db.Column(db.String)
    views = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='article_comments', lazy='dynamic')
    
    def save_article(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_popular(cls):
        return Article.query.limit(5)
    
    @classmethod
    def get_recent(cls):
        return Article.query.limit(10)
    
    @classmethod
    def get_category(cls, category_id):
        return Articles.query.filter_by(category = category_id).limit(5)

    @classmethod
    def get_more_recent(cls, page_number):
        new_limit = page_number * 10
        return Article.query.limit(new_limit)
    
    @classmethod
    def get_more_category(cls, category_id):
        new_limit = page_number * 10
        return Articles.query.filter_by(category = category_id).limit(new_limit)
    
    @classmethod
    def get_related_articles(cls, category_id):
        return Article.query.filter_by(category = category_id).order_by(views.dec).limit(5)
    
    @classmethod
    def get_article(cls, article_id):
        article = Article.query.filter_by(id = article_id).first()
    
        
class Category(db.Model):
    
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    
    def add_category(self):
        db.session.add(self)
        db.session.commit()
        
    def get_categories():
        return Category.query.all()
    
    def get_category(category_id):
        return Category.query.filter_by(id = category_id).first()
    

class Comment(db.Model):
    
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    content = db.Column(db.String)
    
    def add_comment(self):
        db.session.add(self)
        db.session.commit()
        
    def get_article_comments(article_id):
        found_comments = Comment.query.filter_by(article_id = article_id).limit(10)
        comment_list = list()
        for comment in found_comments:
            comment_item = {}
            commentor = User.query.filter_by(id = comment.user_id ).first()
            
            if commentor:
                comment_item['username'] = commentor.user_name
                comment_item['user_avatar'] = commentor.avatar
                comment_item['comment'] = comment.content
                
                comment_list.append(comment_item)
            else:
                print('Problem finding user')
        return comment_list
    
    def get_more_article_comments(article_id, page_number):
        new_limit = 10 * page_number
        found_comments = Comment.query.filter_by(article_id = article_id).limit(new_limit)
        comment_list = list()
        for comment in found_comments:
            comment_item = dict()
            commentor = User.query.filter_by(id = comment.user_id ).first()
            
            comment_item['username'] = commentor.user_name
            comment_item['user_avatar'] = commentor.avatar
            comment_item['comment'] = comment.content
            
            comment_list.append(comment_item)
            
        return comment_list
            
    
class User(db.Model, UserMixin):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    user_email = db.Column(db.String)
    user_pass = db.Column(db.String)
    avatar = db.Column(db.String)
    comments = db.relationship('Comment', backref='comments', lazy='dynamic')
    
    def create_user(self):
        db.session.add(self)
        db.session.commit()
        
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id = user_id).first()
    
    @property
    def password(self, password):
        raise AttributeError('Password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.user_pass = generate_password_hash(password)
        
    def  verify_password(self, password):
        return check_password_hash(self.user_pass, password)        
    


class Quote:
    
    def __init__(self, text, author, tag, image_url):
        self.text = text,
        self.author = author,
        self.tag = tag, 
        self.image_url = image_url