from typing import List, Optional
from app.database.models.user import User, UserRole
from app.database import db


class UserRepository:
    """
    Manages CRUD operations for the User model.
    """

    @staticmethod
    def create(
        username: str,
        email: str,
        password: str,
        name: str,
        avatar_url: Optional[str] = None,
        role=UserRole.USER,
    ) -> User:
        new_user = User(
            username=username, email=email, name=name, avatar_url=avatar_url, role=role
        )
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_by_id(user_id: int) -> Optional[User]:
        return User.query.get(user_id)

    @staticmethod
    def get_by_username(username: str) -> Optional[User]:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_by_email(email: str) -> Optional[User]:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all() -> List[User]:
        return User.query.all()

    @staticmethod
    def update(user_id: int, **kwargs) -> User:
        user = User.query.get(user_id)
        if not user:
            return None

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)

        db.session.commit()
        return user

    @staticmethod
    def delete(user_id: int) -> bool:
        user = User.query.get(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True
