"""Store Item routes module."""

from flask import request

from controllers.store_item_controller import StoreItemController


def store_item_control():
    """URL to collect information about store items or create new one."""
    if request.method == 'POST':
        return StoreItemController.create()
    else:
        return StoreItemController.get_all()


def store_item_manipulation(store_item_id: int):
    """URL to get, update or delete store item information."""
    if request.method == 'GET':
        return StoreItemController.get(store_item_id)
    elif request.method == 'PUT':
        return StoreItemController.update(store_item_id)
    else:
        return StoreItemController.delete(store_item_id)
