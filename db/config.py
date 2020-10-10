import pathlib

DB_PATH: pathlib.Path = pathlib.Path(__file__).parent.absolute() / "users.json"

print(DB_PATH)
