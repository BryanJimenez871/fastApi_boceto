from pydantic import BaseModel, Field
from typing import Optional

class UsersSchema(BaseModel):
    # Pydantic valida automáticamente que sean los tipos correctos
    id: Optional[int] = None
    name: str = Field(..., min_length=3, max_length=100)
    phone: str = Field(..., min_length=9, max_length=20)


