from app import app
from flask import Flask, render_template, redirect, flash
from flask import request, url_for
from sqlalchemy.exc import IntegrityError

from app import db
from app.forms import LoginForm, RegisterForm
from werkzeug.urls import url_parse

from flask_sqlalchemy import SQLAlchemy
from app.models import User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or password')
            return redirect('/login')
        login_user(user,remember=form.remeber_me.data)
        next_page= request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('/')
        return redirect(next_page)
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/search')
    return render_template('login.html', title='Log In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data,form.email.data,form.name.data)
        ne_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Thanks for registrering, You are a registered user now !!')
        return redirect('/login')
    return render_template('register.html', titles = 'Register', form = form)



@app.route('/search', methods =['GET', 'POST'])
def search():
    return render_template('search.html', title='Search')
