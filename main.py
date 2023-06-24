from chempy import Substance, balance_stoichiometry
from fastapi import FastAPI
from classes import Stoichiometry
import json

app = FastAPI()

def responseTemplate(error: bool, message: str, data):
    return {"error": error, "message": message, "data": json.dumps(data, sort_keys=True)}

@app.get("/substance/{substance}")
def read_substance(substance: str):
    try:
        substanceRes = Substance.from_formula(substance)
        substance_data = {
            "name": substanceRes.name,
            "htmlName": str(substanceRes.html_name),
            "unicodeName": substanceRes.unicode_name,
            "composition": str(substanceRes.composition),
            "mass": str(substanceRes.mass),
            "molarMass": str(substanceRes.molar_mass()),
        }
        print(substance_data)
        return responseTemplate(False, f"Información del {substanceRes.name}", substance_data)
    except Exception as e:
        return responseTemplate(True, "Formula inválida", None)


@app.post("/balance-stoichiometry")
async def balanceStoichiometry(stoichiometry: Stoichiometry):
    try:
        reac, prod = balance_stoichiometry(stoichiometry.left, stoichiometry.right)
        print(reac, prod)
        return responseTemplate(False, "", {"reactants": reac, "products": prod})
    except Exception as e:
        return responseTemplate(True, str(e), None)
