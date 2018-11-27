from flask import Flask
from flask import render_template
from database import get_all_cats , create_cat

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html",
    cats=cats,
    'create_cat')


@app.route('/cats/<int:id>')
def cat_1(id):
    return render_template(     
        'cat.html' )


@app.route('/newcat')
def add_cat():
    return render_template(
        'newcat.html')


@app.route('/submit')
def submit_thanks():
    return render_template(
        'submit.html')



if __name__ == '__main__':
    app.run(debug = True)
