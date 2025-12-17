from pydantic import BaseModel
from typing import List, Literal


class UliSlurListConfig(BaseModel):
    type: Literal["uli_slur_list"]
    languages: List[str] = ["en", "hi"]
    severity: Literal["low", "medium", "high"]