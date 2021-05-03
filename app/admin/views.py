from datetime import datetime, date

from flask import render_template, url_for, flask, redirect
from flask_log import login_required
from . import admin
from .forms import CreateNewArticle

from .. import db
from ..models import Article, Category
from ..request import get_pexels_image

@admin.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    new_login = AdminLoginForm()
    
    if new_login.validate_on_submit():
        user = User.query.filter_by(user_email = 'admin').first()
        
        if user is not None and user.verify_password(new_login.password.data):
            login_user(user, new_login.remember_user.data)
            
            return redirect(request.args.get('next') or url_for('admin.index'))
        
        flash('Invalid email or password')
        
    title = 'Welcome back: Pitch Perfect Sign-in'
    
    return render_template('auth/signin.html', form = new_login, title = title)


@login_required
@admin.route('/admin/create-article', methods['GET, POST'])
def create_article():
    title = "Tony's Perspective: Admin"
    
    form = CreateNewArticle()
    
    if form.validate_on_submit():
        new_article_title = form.title.data
        new_article_category = form.category.data
        new_article_content = form.content.data
        new_date = date.today()
        
        selected_category = Category.query.filter_by(id = new_article_category).first()
        
        image_url = get_pexels_image(selected_category.title)
        
        formated_date = new_date.strftime("%a, %d %B, %y")
        
        
        new_article = Article(image_url=image_url ,date=formated_date ,category= new_article_category ,content= new_article_content,views= 0)
        new_article.save_article()
        
        return redirect( url_for('admin.create_article'))
    
    return render_template('admin/create.html' form = form, title = title)