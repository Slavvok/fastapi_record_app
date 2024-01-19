from fastapi import FastAPI
from routes import records

app = FastAPI()


app.include_router(records.router, prefix="/records")
