from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.operation import Operation
import uvicorn

#https://testdriven.io/blog/fastapi-beanie/


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING
    )
    # parte antes do yielt sera executadas antes da inicialização da api
    print("Executa ao iniciar aplicação")
    await init_beanie(database=client.argus, document_models=[Operation])
    tastk1 = Operation(name= "Operação XYZ")
    await tastk1.insert()
    print("Mongodb conected")
    yield
    # Após o yied será executado ao finalizar a aplicação
    print("Executa ao finalizar aplicação")
app = FastAPI(title="API Model with mongodb",lifespan=lifespan)

#app.include_router()
#app.include_router(items.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



