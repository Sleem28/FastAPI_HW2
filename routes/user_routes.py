from fastapi import APIRouter

from db import users, datebase
from models import User, UserIn

user_router = APIRouter()

@user_router.get("/users", response_model=list[User])
async def get_users():
    query = users.select()
    return await datebase.fetch_all(query=query)

@user_router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await datebase.fetch_one(query=query)

@user_router.post("/users", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(
        **user.model_dump()
    )
    last_id = await datebase.execute(query)
    return {**user.model_dump(), "id": last_id}

@user_router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = (
        users.update()
        .where(users.c.id == user_id)
        .values(
            **new_user.model_dump()
        )
    )
    await datebase.execute(query)
    return {**new_user.model_dump(), "id": user_id}

@user_router.delete("/users/{user_id}")
async def user_delete(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await datebase.execute(query)
    return {"message": f"user with {user_id} is deleted"}