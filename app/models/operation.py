from datetime import datetime
from beanie import Document
from typing import List, Optional
from pydantic import BaseModel


class Operation(Document):
    name: str 
    start_date: datetime = datetime.now()
    # end_date: Optional[datetime]
    #picture: Optional[List[str]]  # Agora é uma lista de strings
    
    # class Settings:
    #     name = "operation"

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "Operação XYZ",
    #             "start_date": "2024-04-16T12:00:00",
    #             "end_date": "2024-04-20T12:00:00",
    #             "picture": [
    #                 "https://example.com/picture1.jpg",
    #                 "https://example.com/picture2.jpg",
    #                 "https://example.com/picture3.jpg"
    #             ]  # Exemplo de lista de URLs de imagem
    #         }
    #     }


# class picture(Document):
#     path: str
#     labelmaker: Optional[List[labelmaker]] 
    


    
    

