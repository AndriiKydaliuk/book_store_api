"""Module to manage ORM Store Item model."""

from database import db


class StoreItem(db.Model):
    """Store Item table specification."""

    __tablename__ = "store_items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product = db.Column(db.Integer, db.ForeignKey("products.id"))
    available_qty = db.Column(db.Integer, nullable=False)
    booked_qty = db.Column(db.Integer, nullable=False)
    sold_qty = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<StoreItem {self.product}>"
