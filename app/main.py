from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from routes import products, orders, users

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],   # Allows all headers
)

app.include_router(products.router,  prefix="/api/products", tags=["products"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(orders.router, prefix="/api/orders", tags=["Orders"])
# app.include_router(dashboard_router, prefix="/api/dashboard", tags=["Dashboard"])

@app.get("/")
async def hello():
    return RedirectResponse(url="/docs/")

