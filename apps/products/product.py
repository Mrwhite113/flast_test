from flask_restful import Resource
from flast_test.apps.database.postgres.models import ProductReview, Products
from flast_test.apps.database.postgres.schemas import ProductsSchema, ProductReviewSchema
from flask import jsonify, request


class Products(Resource):

    # def get(self, asin):
    #     print(asin)
        # return jsonify(json_list=[i.serialize for i in ProductReview.query.all()])

    def get(self):#, asin):
        product = Products.query.filter_by(asin="B06X14Z8JP")
        review = ProductReview.query.filter_by(asin="B06X14Z8JP")
        result = ProductsSchema().dump(review)

        return result
