from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user, customer, address, product, reviews
import os


app = FastAPI()

app.include_router(
    user.user, tags=["Users"], prefix="/users",
)

app.include_router(
    customer.customer, tags=["Customers"], prefix="/customers"
)

app.include_router(
    address.address, tags=["Addresses"], prefix="/addresses"
)

app.include_router(
    product.product, tags=["Products"], prefix="/products"
)

app.include_router(
    reviews.review, tags=["Reviews"], prefix="/reviews"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
