from flask import Flask
from flask import render_template
from database import get_all_cats , create_cat

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    new_cat = create_cat('add cat')
    return render_template("home.html", cats=cats)


@app.route('/cats/<int:id>')
def cat_1(id):
	return render_template(
		'cat.html' )


@app.route('/new_cat')
def add_cat():
	return render_template(
		'new_cat.html')

if __name__ == '__main__':
   app.run(debug = True)
