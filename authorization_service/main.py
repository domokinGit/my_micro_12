import mongoengine
from fastapi import FastAPI

from router import router
from fastapi.middleware.cors import CORSMiddleware
from auth_service.router import router as auth_router
from deps import init_tracer
from prometheus_fastapi_instrumentator import Instrumentator

DB_NAME = 'mydb'
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    mongoengine.connect(host=f"mongodb://mongo_users:27017/{DB_NAME}", alias=DB_NAME)
    Instrumentator().instrument(app).expose(app)
    init_tracer()


@app.on_event("shutdown")
async def shutdown():
    mongoengine.disconnect(alias=DB_NAME)


@app.get('/_health')
async def health_check():
    return {
        'status': 'Ok'
    }


app.include_router(router, prefix='/v1')
app.include_router(auth_router, prefix='/v1')
