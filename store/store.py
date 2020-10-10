import json
from dataclasses import asdict
from typing import List

from db.config import DB_PATH
from store.exceptions import ValidationError
from user.model import User


class Store:
    def __init__(self):
        session = Session()

    def buy(self):
        pass

    def login(self, username: str, password: str) -> str:
        with DB_PATH.open("r") as f:
            users = json.load(f)
            for user in users:
                if username in users and password in users:
                    return User(**user)

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        username: str,
        password: str,
        password2: str,
    ) -> str:
        self._validate_password(password, password2)
        if self._is_username_available(username):
            user = self.get_user_obj(first_name, last_name, email, username, password)
            with DB_PATH.open("w") as f:
                json.dump(asdict(user), f)
            return f"{user} Has been registered!"
        else:
            return f"{username} is already taken!"

    def logout(self):
        pass

    def _validate_password(self, password, password2) -> bool:
        if password != password2:
            raise ValidationError("Password mismatch")

    def _is_username_available(self, username: str) -> bool:
        with DB_PATH.open("r") as f:
            users = json.load(f)
        return not any(username in user.values() for user in users)

    def get_user_obj(
        self, first_name: str, last_name: str, email: str, username: str, password: str
    ) -> User:
        return User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )


class Session:
    def __init__(self):
        users = []

    def add_user(self, user) -> None:
        self.users.append(user)
