from flask_login import UserMixin

from . import db
from . import login_manager
from werkzeug import generate_password_hash, check_password_hash

class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key = True)
    image_url = db.Column(db.String)
    title = db.Column(db.String)
    date = db.Column(db.Time)
    author = db.Column(db.String)
    category = db.Column(db.Integer, db.foreignKey('categories.id'))
    content = db.Column(db.String)
    views = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='article_comments', lazy='dynamic')
    
    def save_article(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_popular(cls):
        return(Article.query.order_by(views.dec)).limit(5)
    
    @classmethod
    def get_recent(cls):
        return Article.query.limit(10)
    
    @classmethod
    def get_category(cls, category_id):
        return Articles.query.filter_by(category = category_id).limit(20)

    @classmethod
    def get_more_recent(cls, page_number):
        new_limit = page_number * 10
        return Article.query.limit(new_limit)
    
    @classmethod
    def get_more_category(cls, category_id):
        new_limit = page_number * 10
        return Articles.query.filter_by(category = category_id).limit(new_limit)
    
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
    user_id = db.Column(db.Integer, db.foreignKey('user.id'))
    article_id = db.Column(db.Integer, db.foreignKey('articles.id'))
    content = db.Column(db.String)
    
    def add_comment(self):
        db.session.add(self)
        db.session.commit()
        
    def get_article_comments(article_id):
        return Comment.query.filter_by(article_id = article_id).limit(10)
    
    def get_more_article_comments(article_id, page_number):
        new_limit = 10 * page_number
        
        return Comment.query.filter_by(article_id).limit(new_limit)
