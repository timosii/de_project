import os
from superset import db
from superset.models.core import Database
from dotenv import load_dotenv

load_dotenv()
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DB_NAME = os.environ.get('DB_NAME')

existing_db = db.session.query(Database).filter_by(database_name=f"{DB_NAME}").first()

if not existing_db:
    new_db = Database(
        database_name="DB_NAME",
        sqlalchemy_uri=f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{HOST}:{PORT}/{DB_NAME}",
        extra='{"engine_params": {"connect_args": {"options": "-csearch_path=public"}}}'
    )
    db.session.add(new_db)
    db.session.commit()

print(f"Connection success to {DB_NAME}!")
