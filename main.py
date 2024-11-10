# D:\Test\rest_api\main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from API.ASSES import router as asses_router
from API.RESTAPI import router as restapi_router
from GRAPHQL.GRAPHQL_API import graphql_app as graphql_api_router
from GRAPHQL.GraphQL_ASSES import graphql_app as graphql_asses_router

app = FastAPI()

origins = [
    "https://ved-portal.topgrep.com/",
    "https://portal.topgrep.com/",
    "https://qa-portal.topgrep.com/",
    "https://mockapi.topgrep.com",
    "http://localhost:3000",
    "http://localhost:8005/",
    "http://127.0.0.1:8005/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with prefixes to separate routes
app.include_router(asses_router,prefix="/assessment")
app.include_router(restapi_router,prefix="/api")
app.include_router(graphql_api_router, prefix="/api/graphql")  # Prefix for the first GraphQL API
app.include_router(graphql_asses_router, prefix="/assessment/graphql")

@app.get("/")
async def read_root():
    return "Welcome to Aivagam API Page"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8005, reload=True)