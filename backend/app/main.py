from fastapi import FastAPI

from app.guardrail.validator.registry import (
    ValidatorRegistry,
    load_validator_data
) 

app = FastAPI()

@app.get("/validators")
async def get_validators():
    validator_data = load_validator_data()
    validators = validator_data.validators

    output = []
    for validator in validators:
        validator_config = ValidatorRegistry.get(validator.type)
        output.append({"type": validator.type , "config": validator_config.model_json_schema()})
    return {"validators": output}
