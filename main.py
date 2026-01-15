from Routers.users import router as users_router
from contextlib import asynccontextmanager
from fastapi import FastAPI
from Conexiones.Conexion import Conexion


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    await Conexion.obtener_pool()
    yield
    # SHUTDOWN
    await Conexion.cerrar_pool()

app = FastAPI(
    title="Proyecto API",
    version="1.0.0",
    lifespan=lifespan
)

# Registrar routers
app.include_router(users_router)

