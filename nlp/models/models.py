from pydantic import BaseModel
from typing import List, Optional

class TextInput(BaseModel):
    text: str

class ClassificationInput(BaseModel):
    text: str
    labels: Optional[List[str]] = None