import mongoengine
from fastapi import FastAPI

from deps import init_tracer
from router import router
from fastapi.middleware.cors import CORSMiddleware

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
    mongoengine.connect(host=f"mongodb://mongo_menu:27017/{DB_NAME}", alias=DB_NAME)
    Instrumentator().instrument(app).expose(app)
    init_tracer()


@app.on_event("shutdown")
async def shutdown():
    mongoengine.disconnect(alias=DB_NAME)


app.include_router(router, prefix='/v1')


@app.get('/_health')
async def health_check():
    return {
        'status': 'Ok'
    }
