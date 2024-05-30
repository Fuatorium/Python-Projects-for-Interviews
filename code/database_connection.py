from sqlalchemy import create_engine
import pandas as pd

DATABASE_URI = 'mysql+pymysql://root:patatesroot@localhost:3306/mydatabase'  # root kullanıcı adı ve yeni şifre
engine = create_engine(DATABASE_URI)

def fetch_data(query):
    with engine.connect() as connection:
        return pd.read_sql(query, connection)

def insert_data(name, email):
    with engine.connect() as connection:
        query = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
        connection.execute(query)

def fetch_all_users():
    query = "SELECT * FROM users"
    return fetch_data(query)