from flask import Flask
from flask_restful import Resource, reqparse, Api
from flast_test.apps.database.postgres.connection import get_connection_str
from flask_sqlalchemy import SQLAlchemy
from flast_test.apps.products.product import Products
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_str()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma = Marshmallow(app)


api = Api(app)


api.add_resource(Products, '/api/product/', endpoint='product')



if __name__ == '__main__':

    app.run(debug=True)






