"""Module to manage ORM Product model."""

from database import db


class Product(db.Model):
    """Product table specification."""

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(256), nullable=False)
    price = db.Column(db.Float(256), nullable=False)
    image_path = db.Column(db.String(256), nullable=False)
    store_item = db.relationship('StoreItem', backref='products', lazy=True)

    def __repr__(self) -> str:
        return f"<Product {self.description}>"
