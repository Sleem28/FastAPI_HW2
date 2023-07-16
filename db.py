from sqlalchemy import Column, Integer, String, Boolean, create_engine, MetaData, Table, ForeignKey, Date, Float
import databases as databases

from settings import settings

DATABASE_URL = settings.DATABASE_URL
datebase = databases.Database(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(20)),
    Column("last_name", String(20)),
    Column("email", String(30)),
    Column("password", String(150)),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("description", String(500)),
    Column("price", Float)
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id")),
    Column("product_id", ForeignKey("products.id")),
    Column("create_date", Date),
    Column("status", Boolean),
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
