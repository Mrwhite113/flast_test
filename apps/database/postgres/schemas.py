from flast_test.main import ma
from flast_test.apps.database.postgres.models import Products, ProductReview


class ProductsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Products

    asin = ma.auto_field()
    title = ma.auto_field()
    review = ma.auto_field()


class ProductReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductReview
        include_fk = True
