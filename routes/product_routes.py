from fastapi import APIRouter

from db import products, datebase
from models import Product, ProductIn

product_router = APIRouter()

@product_router.get("/products", response_model=list[Product])
async def get_products():
    query = products.select()
    return await datebase.fetch_all(query=query)

@product_router.get("/products/{product_id}", response_model=list[Product])
async def get_product_by_id(product_id: int):
    query = products.select().where(products.id == product_id)
    return await datebase.fetch_one(query=query)

@product_router.post("/products", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(**product.model_dump())
    product_id = await datebase.execute(query)
    return {**product.model_dump(), "id": product_id}

@product_router.put("/products/{product_id}", response_model=Product)
async def change_product(product_id: int, product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**product.model_dump())
    await datebase.execute(query)
    return {**product.model_dump(), "id": product_id}

@product_router.delete("/products/{product_id}")
async def delete_products(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await datebase.execute(query)
    return {"message": f"Product with {product_id} is deleted"}
