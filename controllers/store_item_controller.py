"""Controller module."""

from services.store_item_service import StoreItemService


class StoreItemController:
    """Class to communicate directly with the services."""

    @staticmethod
    def get(store_item_id: int):
        """Get store_item resource."""
        return StoreItemService.get(store_item_id)

    @staticmethod
    # @auth.login_required
    def get_all():
        """Get all store_item resources."""
        return StoreItemService.get_all()

    @staticmethod
    def create():
        """Create store_item resource."""
        return StoreItemService.create()

    @staticmethod
    def delete(store_item_id: int):
        """Delete store_item resource."""
        return StoreItemService.delete(store_item_id)

    @staticmethod
    def update(store_item_id: int):
        """Update store_item resource."""
        return StoreItemService.update(store_item_id)
