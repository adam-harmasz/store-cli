import json
from dataclasses import dataclass

from db.config import DB_PATH


@dataclass
class User:
    first_name: str
    last_name: str
    username: str
    email: str
    password: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return self.full_name


with DB_PATH.open("r") as f:
    username = "adam.harmasz"
    password = "12qwerty12"
    users = json.load(f)
    for user in users:
        print(user)
        if username == user["username"] and password == user["password"]:
            print(User(**user))
            print("DUPSKO")
        else:
            print("OJ")