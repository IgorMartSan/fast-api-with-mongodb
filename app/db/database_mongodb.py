from beanie import init_beanie
import motor.motor_asyncio

from  models.operation import 




async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://root:example@mongo:27017/"
    )

    await init_beanie(database=client.db_name, document_models=[ProductReview])