"""Services module."""

from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from data_access_objects.product_dao import ProductDao
from schemas.schemas import ProductSchema

# schema to manage single model data
productSchema = ProductSchema()
# schema to manage multiple models data
productListSchema = ProductSchema(many=True)


class ProductService:
    """To support CRUD operations for product model."""

    @staticmethod
    def get(product_id: int):
        """Get product resource"""
        product_data = ProductDao.fetch_by_id(product_id)
        return productSchema.dump(product_data)

    @staticmethod
    def get_all():
        """Get all product resources"""
        return productListSchema.dump(ProductDao.fetch_all())

    @staticmethod
    def create():
        """Create product resource"""
        product_req_json = request.get_json()
        product_data = productSchema.load(product_req_json)
        ProductDao.create(product_data)
        return productSchema.dump(product_data), 201

    @staticmethod
    def delete(product_id: int):
        """Delete product resource"""
        ProductDao.fetch_by_id(product_id)
        ProductDao.delete(product_id)
        return {'message': 'Product deleted successfully'}, 200

    @staticmethod
    def update(product_id: int):
        """Update product resource"""
        try:
            product_data = productSchema.dump(ProductDao.fetch_by_id(product_id))
            product_data.update(request.get_json())
            product_data = productSchema.load(product_data)
            ProductDao.update(product_data)
            return productSchema.dump(product_data), 204
        except ValidationError as error:
            return jsonify(detail=str(error), status=400, title="Bad Request", type="about:blank")
        except IntegrityError as error:
            return jsonify(detail=error.args[0], status=400, title="Bad Request", type="about:blank")
