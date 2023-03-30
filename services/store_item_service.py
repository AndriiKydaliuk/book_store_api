"""Services module."""

from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from data_access_objects.store_item_dao import StoreItemDao
from schemas.schemas import StoreItemSchema

# schema to manage single model data
store_itemSchema = StoreItemSchema()
# schema to manage multiple models data
store_itemListSchema = StoreItemSchema(many=True)


class StoreItemService:
    """To support CRUD operations for store item model."""

    @staticmethod
    def get(store_item_id: int):
        """Get store item resource"""
        store_item_data = StoreItemDao.fetch_by_id(store_item_id)
        return store_itemSchema.dump(store_item_data)

    @staticmethod
    def get_all():
        """Get all store item resources"""
        return store_itemListSchema.dump(StoreItemDao.fetch_all())

    @staticmethod
    def create():
        """Create store item resource"""
        store_item_req_json = request.get_json()
        store_item_data = store_itemSchema.load(store_item_req_json)
        StoreItemDao.create(store_item_data)
        return store_itemSchema.dump(store_item_data), 201

    @staticmethod
    def delete(store_item_id: int):
        """Delete store item resource"""
        StoreItemDao.fetch_by_id(store_item_id)
        StoreItemDao.delete(store_item_id)
        return {'message': 'Store Item deleted successfully'}, 200

    @staticmethod
    def update(store_item_id: int):
        """Update store item resource"""
        try:
            store_item_data = store_itemSchema.dump(StoreItemDao.fetch_by_id(store_item_id))
            store_item_data.update(request.get_json())
            store_item_data = store_itemSchema.load(store_item_data)
            StoreItemDao.update(store_item_data)
            return store_itemSchema.dump(store_item_data), 204
        except ValidationError as error:
            return jsonify(detail=str(error), status=400, title="Bad Request", type="about:blank")
        except IntegrityError as error:
            return jsonify(detail=error.args[0], status=400, title="Bad Request", type="about:blank")
