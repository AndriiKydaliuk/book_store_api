"""
Module for Product Store Item Access Object.
"""

from database import db
from models.store_item_model import StoreItem
from typing import List


class StoreItemDao:
    """
    Data Access Object class for StoreItem Model.
    """

    STORE_ITEM_NOT_FOUND = "Store Item not found for id: {}"

    @staticmethod
    def create(store_item: StoreItem):
        """Creates store item in database"""
        db.session.add(store_item)
        db.session.commit()

    @staticmethod
    def fetch_by_id(store_item_id: int) -> StoreItem:
        """Gets store item by id from database"""
        return db.session.query(StoreItem).get_or_404(
            store_item_id,
            description=StoreItemDao.STORE_ITEM_NOT_FOUND.format(store_item_id)
        )

    @staticmethod
    def fetch_all() -> List[StoreItem]:
        """Returns all store items from database"""
        return db.session.query(StoreItem).all()

    @staticmethod
    def delete(store_item_id) -> None:
        """Deletes store item from database"""
        item = db.session.query(StoreItem).filter_by(id=store_item_id).first()
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def update(store_item_data):
        """Updates store item in database"""
        db.session.merge(store_item_data)
        db.session.commit()
