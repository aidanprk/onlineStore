from flask import *
from flask_sqlalchemy import  *
from server.scripts.models import db, Deck
import time


app = Flask(__name__)
title = "Portland Skateboards"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/aidan/PycharmProjects/hangman/server/database.db'

db.app = app
db.init_app(app)

product_1 = Deck.query.filter_by(id=1).first()
product_2 = Deck.query.filter_by(id=2).first()
product_3 = Deck.query.filter_by(id=3).first()
featured = [product_1, product_2, product_3]



@app.route("/")
def home():
    return render_template('store.html', title=title, featured = featured)

@app.route('/add_product')
def addProductPage():
    return render_template('temp_add_product.html')

@app.route('/submit', methods=['POST'])
def addProduct():

    name = request.form['name']
    desc = request.form['desc']
    price = request.form['price']
    img1 = request.form['imgFront']
    img2 = request.form['imgBack']

    newProduct = Deck(name, desc, float(price), img1, img2)
    db.session.add(newProduct)
    db.session.commit()

    return '<p> Complete </p>'
    time.sleep(5)
    return redirect(url_for('home'))

@app.route('/products')
def products():
    return str(Deck.query.all())


app.run(debug=True, port=1130)