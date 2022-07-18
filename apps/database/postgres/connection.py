import os
from sqlalchemy import create_engine, select, MetaData, Table, and_
from dotenv import load_dotenv
load_dotenv()


def get_db_connection():
    db_string = "postgresql://{user}:{paswrd}@{ip}:{port}/{db_name}".format(
        user=os.getenv("POSTGRES_USER"),
        paswrd=os.getenv("POSTGRES_PASS"),
        ip=os.getenv("IP"),
        port=os.getenv("PORT"),
        db_name=os.getenv("POSTGRES_DB"),
    )
    db = create_engine(db_string)
    return db


def get_connection_str():
    conn_string = "postgresql://{user}:{paswrd}@{ip}:{port}/{db_name}".format(
        user=os.getenv("POSTGRES_USER"),
        paswrd=os.getenv("POSTGRES_PASS"),
        ip=os.getenv("IP"),
        port=os.getenv("PORT"),
        db_name=os.getenv("POSTGRES_DB"),
    )
    return conn_string


# def get_model_data(table=None):
#     engine = create_engine(get_db_connection())
#     metadata = MetaData(bind=None)
#     selected_table = Table(
#         table,
#         metadata,
#         autoload=True,
#         autoload_with=engine
#     )
#     return selected_table