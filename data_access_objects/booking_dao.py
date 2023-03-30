"""
Module for Booking Data Access Object.
"""

from database import db
from models.booking_model import Booking
from typing import List


class BookingDao:
    """
    Data Access Object class for Booking Model.
    """

    BOOKING_NOT_FOUND = "Booking not found for id: {}"

    @staticmethod
    def create(booking: Booking):
        """Creates booking in database"""
        db.session.add(booking)
        db.session.commit()

    @staticmethod
    def fetch_by_id(booking_id: int) -> Booking:
        """Gets booking by id from database"""
        return db.session.query(Booking).get_or_404(
            booking_id,
            description=BookingDao.BOOKING_NOT_FOUND.format(booking_id)
        )

    @staticmethod
    def fetch_all() -> List[Booking]:
        """Returns all bookings from database"""
        return db.session.query(Booking).all()

    @staticmethod
    def delete(booking_id) -> None:
        """Deletes booking from database"""
        item = db.session.query(Booking).filter_by(id=booking_id).first()
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def update(booking_data):
        """Updates booking in database"""
        db.session.merge(booking_data)
        db.session.commit()
