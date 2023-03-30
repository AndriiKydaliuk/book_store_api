"""Controller module."""

from services.booking_service import BookingService


class BookingController:
    """Class to communicate directly with the services."""

    @staticmethod
    def get(booking_id: int):
        """Get booking resource."""
        return BookingService.get(booking_id)

    @staticmethod
    # @auth.login_required
    def get_all():
        """Get all booking resources."""
        return BookingService.get_all()

    @staticmethod
    def create():
        """Create booking resource."""
        return BookingService.create()

    @staticmethod
    def delete(booking_id: int):
        """Delete booking resource."""
        return BookingService.delete(booking_id)

    @staticmethod
    def update(booking_id: int):
        """Update booking resource."""
        return BookingService.update(booking_id)
