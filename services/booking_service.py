"""Services module."""

from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from data_access_objects.booking_dao import BookingDao
from schemas.schemas import BookingSchema

# schema to manage single model data
bookingSchema = BookingSchema()
# schema to manage multiple models data
bookingListSchema = BookingSchema(many=True)


class BookingService:
    """To support CRUD operations for store item model."""

    @staticmethod
    def get(booking_id: int):
        """Get booking resource"""
        booking_data = BookingDao.fetch_by_id(booking_id)
        return BookingSchema.dump(booking_data)

    @staticmethod
    def get_all():
        """Get all booking resources"""
        return bookingListSchema.dump(BookingDao.fetch_all())

    @staticmethod
    def create():
        """Create booking resource"""
        booking_req_json = request.get_json()
        booking_data = bookingSchema.load(booking_req_json)
        BookingDao.create(booking_data)
        return bookingSchema.dump(booking_data), 201

    @staticmethod
    def delete(booking_id: int):
        """Delete booking resource"""
        BookingDao.fetch_by_id(booking_id)
        BookingDao.delete(booking_id)
        return {'message': 'Booking deleted successfully'}, 200

    @staticmethod
    def update(booking_id: int):
        """Update booking resource"""
        try:
            booking_data = bookingSchema.dump(BookingDao.fetch_by_id(booking_id))
            booking_data.update(request.get_json())
            booking_data = bookingSchema.load(booking_data)
            BookingDao.update(booking_data)
            return bookingSchema.dump(booking_data), 204
        except ValidationError as error:
            return jsonify(detail=str(error), status=400, title="Bad Request", type="about:blank")
        except IntegrityError as error:
            return jsonify(detail=error.args[0], status=400, title="Bad Request", type="about:blank")
