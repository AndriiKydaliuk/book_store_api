"""
ORM Schemas.
"""
from marshmallow_enum import EnumField

from database import db
from dependencies import ma
from models.user_model import User, Role
from models.product_model import Product
from models.store_item_model import StoreItem
from models.booking_model import Booking


class UserSchema(ma.SQLAlchemySchema):
    """User schema."""

    class Meta:
        model = User  # The SQLAlchemy model to generate the Schema from.
        load_instance = True  # Whether to load model instances (deserialize to an object).
        sqla_session = db.session

    id = ma.auto_field()
    name = ma.auto_field()
    role = EnumField(Role)
    email = ma.auto_field()
    phone = ma.auto_field()
    address = ma.auto_field()
    login = ma.auto_field()


class ProductSchema(ma.SQLAlchemySchema):
    """Product schema."""

    class Meta:
        model = Product  # The SQLAlchemy model to generate the Schema from.
        load_instance = True  # Whether to load model instances (deserialize to an object).
        sqla_session = db.session

    id = ma.auto_field()
    name = ma.auto_field()
    description = ma.auto_field()
    author = ma.auto_field()
    price = ma.auto_field()
    image_path = ma.auto_field()


class StoreItemSchema(ma.SQLAlchemySchema):
    """Store Item schema."""

    class Meta:
        model = StoreItem  # The SQLAlchemy model to generate the Schema from.
        load_instance = True  # Whether to load model instances (deserialize to an object).
        sqla_session = db.session

    id = ma.auto_field()
    product = ma.auto_field()
    available_qty = ma.auto_field()
    booked_qty = ma.auto_field()
    sold_qty = ma.auto_field()


class BookingSchema(ma.SQLAlchemySchema):
    """Booking schema."""

    class Meta:
        model = Booking  # The SQLAlchemy model to generate the Schema from.
        load_instance = True  # Whether to load model instances (deserialize to an object).
        sqla_session = db.session

    id = ma.auto_field()
    product = ma.auto_field()
    description = ma.auto_field()
    user = ma.auto_field()
    delivery_address = ma.auto_field()
    delivery_date = ma.auto_field()
    delivery_datetime = ma.auto_field()
    status_id = ma.auto_field()
    quantity = ma.auto_field()
