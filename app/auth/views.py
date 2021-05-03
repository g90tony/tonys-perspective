from flask import render_template, url_for,flash, redirect
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import LoginForm, RegistrationForm, AdminLoginForm
from .. import db
from ..email import welcome_message
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    new_login = LoginForm()
    
    if new_login.validate_on_submit():
        user = User.query.filter_by(user_email = new_login.email.data).first()
        
        if user is not None and user.verify_password(new_login.password.data):
            login_user(user, new_login.remember_user.data)
            
            return redirect(request.args.get('next') or url_for('main.index'))
        
        flash('Invalid email or password')
        
    title = 'Welcome back: Pitch Perfect Sign-in'
    
    return render_template('auth/signin.html', form = new_login, title = title)



@auth.route('/register', methods=['GET', 'POST'])
def register():
    new_user = RegistrationForm()
    
    if new_user.validate_on_submit():
       
        user = User(username = f'{new_user.first_name.data} {new_user.last_name.data}' ,user_email = new_user.email.data ,bio = '' ,avatar = 'images/avatar.png' ,password = new_user.password.data) 
        user.create_new_user()
 
        
        welcome_message('Welcome to Pitch Perfect', 'email/welcome_user', user.user_email, user= user)
        
        return redirect(url_for('auth.login'))
    
    title = 'Create an account: Pitch Perfect Sign-up'     
    
    return render_template('auth/signup.html', form = new_user, title= title)

@auth.route('/logoff')
def logoff():
    logout_user()
    return redirect(url_for('main.landing'))