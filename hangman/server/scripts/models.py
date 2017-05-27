from flask import *
from flask_sqlalchemy import *

#'http://flask.pocoo.org/docs/0.12/patterns/sqlalchemy/'

db = SQLAlchemy()

class Deck(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    desc = db.Column(db.String(400))
    price = db.Column(db.Float)

    img_front = db.Column(db.String(20))
    img_back = db.Column(db.String(20))

    def __init__(self, name, desc, price, img1, img2):

        self.name = name
        self.desc = desc
        self.price = price
        self.img_front = img1
        self.img_back = img2
        self.markup = '''<div class="product">
                            <h2 class="name">{}</h2>
                            <h3 class="size">8.0</h3>

                            <img src={} />
                            <a href="" class="price">{}</a>
                            <p class="details">{}</p>
                        </div>'''.format(self.name,self.img_back, self.price,self.desc)

    def __repr__(self):
        return self.markup






