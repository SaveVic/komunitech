from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import db


class BaseModel(db.Model):
    """
    A base model for other database models to inherit.
    Includes 'created_at' and 'updated_at' timestamp fields.
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[str] = mapped_column(
        db.DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[str] = mapped_column(
        db.DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )
