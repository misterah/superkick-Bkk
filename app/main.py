from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from routes import products

# docker-compose up --build for upadate
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],   # Allows all headers
)

app.include_router(products.router,  prefix="/api/products", tags=["products"])

@app.get("/")
async def hello():
    return RedirectResponse(url="/docs/")
