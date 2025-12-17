from pydantic import BaseModel
from typing import List, Literal


class PIIBanConfig(BaseModel):
    type: Literal["pii_ban"]
    threshold: float= 0.5
    language: str = "en"