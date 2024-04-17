
from datetime import datetime
from beanie import Document
from typing import List, Optional
from models.picture import picture

class Author(Document):
    name: str = Indexed(unique=True)
    is_human: bool 