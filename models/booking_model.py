"""Module to manage ORM Booking model."""

import enum

from database import db


class BookingStatus(enum.Enum):
    SUBMITTED = 1
    REJECTED = 2
    APPROVED = 3
    CANCELLED = 4
    IN_DELIVERY = 5


class Booking(db.Model):
    """Booking table specification."""

    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product = db.Column(db.Integer, db.ForeignKey("products.id"))
    description = db.Column(db.String(256), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    delivery_address = db.Column(db.String, nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False)
    delivery_datetime = db.Column(db.DateTime, nullable=False)
    status_id = db.Column(db.Enum(BookingStatus), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.status_id}>"

