from fastapi import FastAPI
import uvicorn
from routes import user_router, product_router, order_router
from db import datebase

app = FastAPI()


@app.on_event("startup")
async def startup():
    await datebase.connect()


@app.on_event("shutdown")
async def shutdown():
    await datebase.disconnect()

app.include_router(user_router, tags=["users"])
app.include_router(product_router, tags=["products"])
app.include_router(order_router, tags=["orders"])


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )