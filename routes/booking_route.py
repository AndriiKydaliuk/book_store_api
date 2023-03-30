"""Booking routes module."""

from flask import request

from controllers.booking_controller import BookingController


def booking_control():
    """URL to collect information about bookings or create new one."""
    if request.method == 'POST':
        return BookingController.create()
    else:
        return BookingController.get_all()


def booking_manipulation(booking_id: int):
    """URL to get, update or delete booking information."""
    if request.method == 'GET':
        return BookingController.get(booking_id)
    elif request.method == 'PUT':
        return BookingController.update(booking_id)
    else:
        return BookingController.delete(booking_id)
