"""Controller module."""

from services.product_service import ProductService


class ProductController:
    """Class to communicate directly with the services."""

    @staticmethod
    def get(product_id: int):
        """Get product resource."""
        return ProductService.get(product_id)

    @staticmethod
    # @auth.login_required
    def get_all():
        """Get all product resources."""
        return ProductService.get_all()

    @staticmethod
    def create():
        """Create product resource."""
        return ProductService.create()

    @staticmethod
    def delete(product_id: int):
        """Delete product resource."""
        return ProductService.delete(product_id)

    @staticmethod
    def update(product_id: int):
        """Update product resource."""
        return ProductService.update(product_id)
