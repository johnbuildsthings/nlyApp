from flask import render_template
from . import main

pages = ['home', 'intern', 'wednesday night', 'house party']

@main.route('/')
@main.route('/home')
def index():
    text = 'welcome to nly'
    title = 'NLY'
    
    return render_template('home.html',
                            text=text,
                            title=title,
                            pages=pages)
                            
@main.route('/intern')
def intern():
    text = 'this is the intern page'
    title = 'Intern'
    return render_template('intern.html',
                            text=text,
                            title=title,
                            pages=pages)
                            
@main.route('/wednesday night')
def wedNight():
    text = 'welcome to wednesday night service'
    title = 'Wednesday Night'
    return render_template('wednight.html',
                            text=text,
                            title=title,
                            pages=pages)
                            
@main.route('/house party')
def houseparty():
    text = 'this is where we hang for house parties'
    title = 'House Party'
    return render_template('houseparty.html',
                            text=text,
                            title=title,
                            pages=pages)