from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class Board:
    letters: list[list[str]]

class ChatRequest(BaseModel):
    message: str
    
