
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm
from flask_debug import Debug


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '01ca564fac9185a04f417ae3211ba8f6'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

from models import User, Post



               
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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect (url_for('home'))
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



if __name__ == "__main__":
    app.run(debug=True)