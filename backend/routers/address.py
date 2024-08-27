# TODO: Test routers
from fastapi import APIRouter
from models.customer import Address
from utils.crud_operations import find_all, find_one, create, update, soft_delete, hard_delete

address = APIRouter()

@address.get("/")
async def find_all_addresss():
    return find_all("address")

@address.get("/{id}")
async def find_one_address(id):
    return find_one("address", id)

@address.post("/")
async def create_address(address: Address):
    print(f"Address Data: {address}")
    return create("address", address)

@address.put("/{id}")
async def update_address(id, address: Address):
    return update("address", id, address)

@address.delete("/soft/{id}")
async def soft_delete_address(id):
    return soft_delete("address", id)

@address.delete("/hard/{id}")
async def hard_delete_address(id):
    return hard_delete("address", id)
