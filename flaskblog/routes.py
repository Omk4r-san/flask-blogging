from flaskblog.models import User, Post
from flaskblog import app,db, bcrypt
from flask import  render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm



               
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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@gmail.com" and form.password.data=="12345678":
            flash(f'you have logged in','success')
            return redirect (url_for('home'))
        else:
            flash(f'invalid details', 'danger')    
    return render_template('login.html', title='login', form = form)    

