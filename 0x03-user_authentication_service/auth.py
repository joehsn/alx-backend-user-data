#!/usr/bin/env python3
"""Auth module.
"""
from db import DB
from user import User
from typing import Optional
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hashes a password using bcrypt.
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with an email and password.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError()
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email, hashed_password.decode('utf-8'))
            return user
