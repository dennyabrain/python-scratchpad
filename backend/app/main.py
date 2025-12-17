from fastapi import FastAPI

from app.guardrail.validator.models.pii_ban import PIIBanConfig
from app.guardrail.validator.models.uli_slur_list import UliSlurListConfig 
from app.guardrail.validator.registry import ValidatorRegistry
from app.guardrail.validator.registry import load_validator_data

app = FastAPI()

@app.get("/validators")
async def get_validators():
    validator_data = load_validator_data()
    validators = validator_data.get("validators", [])
    registry = ValidatorRegistry()

    output = []
    for validator in validators:
        validator_type = validator.get("type")
        validator_config = registry.get(validator_type)
        output.append({"type": validator_type, "config": validator_config.model_json_schema()})
    return {"validators": output}
    # return {"validators": PIIBanConfig.model_json_schema()}
