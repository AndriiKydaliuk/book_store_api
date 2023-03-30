"""
Module for Product Data Access Object.
"""

from database import db
from models.product_model import Product
from typing import List


class ProductDao:
    """
    Data Access Object class for Product Model.
    """

    PRODUCT_NOT_FOUND = "Product not found for id: {}"

    @staticmethod
    def create(product: Product):
        """Creates product in database"""
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def fetch_by_id(product_id: int) -> Product:
        """Gets product by id from database"""
        return db.session.query(Product).get_or_404(
            product_id,
            description=ProductDao.PRODUCT_NOT_FOUND.format(product_id)
        )

    @staticmethod
    def fetch_all() -> List[Product]:
        """Returns all products from database"""
        return db.session.query(Product).all()

    @staticmethod
    def delete(product_id) -> None:
        """Deletes product from database"""
        item = db.session.query(Product).filter_by(id=product_id).first()
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def update(product_data):
        """Updates product in database"""
        db.session.merge(product_data)
        db.session.commit()
