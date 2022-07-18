import pandas as pd
from flast_test.apps.database.postgres.models import Products, ProductReview, db


def parse_products():
    key = "1roypo_8amDEIYc-RFCQrb3WyubMErd3bxNCJroX-HVE"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{key}/export?format=csv").to_dict("records")
    return df


def parse_reviews():
    key = "1iSR0bR0TO5C3CfNv-k1bxrKLD5SuYt_2HXhI2yq15Kg"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{key}/export?format=csv").to_dict("records")
    return df


def concat_dict():
    products = parse_products()
    reviews = parse_reviews()
    for p in products:
        p.update({"reviews": []})
        ind_p = p.get('Asin')
        for r in reviews:
            if r.get("Asin") == ind_p:
                p["reviews"].append(r)
    return products


def inset_data():
    data = concat_dict()
    product_list = []
    reviews = []
    for d in data:
        product_list.append(Products(asin=d.get("Asin"), title=d.get("Title")))
        for review in d['reviews']:
            reviews.append(ProductReview(asin=d["Asin"], title=review.get("Title"), review=review.get("Review")))
    db.session.add_all(product_list)
    db.session.add_all(reviews)
    db.session.commit()


inset_data()
