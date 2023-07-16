from fastapi import APIRouter

from db import orders, datebase
from models import Order, OrderIn

order_router = APIRouter()

@order_router.get("/orders", response_model=list[Order])
async def get_orders():
    query = orders.select()
    return await datebase.fetch_all(query=query)

@order_router.get("/orders/{order_id}", response_model=Order)
async def get_order_by_id(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await datebase.fetch_one(query=query)

@order_router.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.model_dump())
    last_id = await datebase.execute(query)
    return {**order.model_dump(), "id": last_id}

@order_router.put("/orders/{order_id}", response_model=Order)
async def change_order(order: OrderIn):
    query = orders.insert().values(**order.model_dump())
    last_id = await datebase.execute(query)
    return {**order.model_dump(), "id": last_id}

@order_router.delete("/orders/{order_id}")
async def delete_orders(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    return await datebase.fetch_all(query=query)