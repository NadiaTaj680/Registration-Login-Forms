from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app=Flask(__name__)

app.config['SECRET_KEY']= 'd262513885bd2427b0e51efa1e150aeb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4321@localhost/Blog_app'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)

posts = [
    {
        'author':'Ali',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20 2018'
    },
    {
        'author':'Khan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20 2018'
    }
]
@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html' , posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login',form=form)


if __name__ =='__main__':
    app.run(debug=True)