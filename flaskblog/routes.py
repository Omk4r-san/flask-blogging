from flaskblog.models import User, Post
from flaskblog import app,db, bcrypt
from flask import  render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required



               
posts = [
    {
        'author': 'Omkar Prasad',
        'title': 'Blog Post 1',
        'content': 'The first post',
        'on_date': '1st Jan 2020',
    },
    {
        'author': 'Kunal Yadav',
        'title': 'Blog Post 2',
        'content': 'The second post',
        'on_date': '2nd Jan 2020',
    },
    {
        'author': 'Rima Bhowmik',
        'title': 'Blog Post 3',
        'content': 'The third post',
        'on_date': '3rd Jan 2020',
    },



]


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('About.html', title='About')

@app.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home')) 

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user  = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account has been created u are now able to login!', 'success')
        return redirect (url_for('login'))
    return render_template('register.html', title='register', form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home')) 

    form = LoginForm()
    if form.validate_on_submit():
       user = User.query.filter_by(email=form.email.data).first()
       if user and bcrypt.check_password_hash(user.password, form.password.data):
          login_user(user, remember= form.remember.data)
          flash(f'login succesful', 'success') 
          return redirect(url_for('home'))
             
       else:
           flash(f'login unssuccesful pease check your email and password', 'danger')    
    return render_template('login.html', title='login', form = form)    


@app.route('/logout')
def logout():
    logout_user()
    flash(f'Logged out successfully', 'primary' )
    return redirect(url_for('home'))


@app.route('/account')
@login_required 
def account():
    return render_template('account.html', title='Account')
