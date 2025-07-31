import enum
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum
from .base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


# Define an Enum for user roles
class UserRole(enum.Enum):
    USER = "user"
    ADMIN = "admin"
    DEVELOPER = "developer"


class User(BaseModel, UserMixin):
    """
    User model representing the users table in the database.
    """

    __tablename__ = "users"

    # Define table columns
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar_url: Mapped[str] = mapped_column(String(255), nullable=True)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole), default=UserRole.USER, nullable=False
    )

    def set_password(self, password: str):
        self.password = generate_password_hash(password, method="pbkdf2:sha256")

    def check_password(self, password: str):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}>"
