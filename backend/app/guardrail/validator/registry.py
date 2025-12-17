from pydantic import BaseModel
from pathlib import Path
import json

from app.guardrail.validator.models.pii_ban import PIIBanConfig
from app.guardrail.validator.models.uli_slur_list import UliSlurListConfig 

class ValidatorRegistry:
    PII_BAN = "pii_ban"
    ULI_SLUR_LIST = "uli_slur_list"
    BAN_LIST = "ban_list"

    _registry = {
        PII_BAN: PIIBanConfig,
        ULI_SLUR_LIST: UliSlurListConfig
    }

    @classmethod
    def get(cls, name: str):
        return cls._registry.get(name)


def load_validator_data() -> dict:
    data_file_path = Path(__file__).parent / "data.json"
    print(data_file_path)
    try: 
        with open(data_file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Error: Validator data file not found at {data_file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Error: Failed to decode JSON from {data_file_path} : {e}")
        raise
