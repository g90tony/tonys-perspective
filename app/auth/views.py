from flask import render_template, url_for,flash, redirect
from flask_login import login_user, logout_user, login_required, current_user

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
        
    title = 'Welcome back: Tonys Perspective Sign-in'
    
    return redirect(url_for('main.index', user=current_user))



@auth.route('/register', methods=['GET', 'POST'])
def register():
    new_registration = RegistrationForm()
    
    if new_registration.validate_on_submit():
       
        user = User(user_name = f'{new_registration.first_name.data} {new_registration.last_name.data}' ,user_email = new_registration.email.data, avatar = 'images/avatar.png' ,user_pass = new_registration.password.data) 
        user.create_user()
 
        
        welcome_message("Welcome to Tony's Perspective", 'email/welcome_user', user.user_email, user= user)
        
        return redirect(url_for('auth.login'))
    
    title = "Create an account: Tony's Perspective Sign-up"     
    
    return render_template('auth/signup.html', form = new_registration, title= title)

@auth.route('/logoff')
def logoff():
    logout_user()
    return redirect(url_for('main.index'))