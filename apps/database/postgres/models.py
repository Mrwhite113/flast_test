from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flast_test.apps.database.postgres.connection import get_connection_str

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_str()
db = SQLAlchemy(app)


class Products(db.Model):
    # __tablename__ = "products"

    asin = db.Column("asin", db.String(60), primary_key=True, unique=True)
    title = db.Column(db.String(300))
    # review = db.relationship('ProductReview', backref='products')

    def __repr__(self):
        return f'<Product "{self.asin}">'


class ProductReview(db.Model):
    # __tablename__ = "product_review"

    id = db.Column('review_id', db.Integer, primary_key=True)
    asin = db.Column(db.String(60), db.ForeignKey("products.asin"))
    title = db.Column(db.String(300))
    review = db.Column(db.String(10000))
    product = db.relationship("Products", backref="productreview")

    def __repr__(self):
        return f'<Review {self.id} product "{self.asin}">'


db.create_all()