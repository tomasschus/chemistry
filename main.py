from chempy import Substance, balance_stoichiometry
from fastapi import FastAPI
from classes import Stoichiometry

app = FastAPI()

def responseTemplate(error, data):
    return {error, data}

@app.get("/substance/{substance}")
def read_root(substance: str):
    try:
        ferricyanide = Substance.from_formula(substance)
        return responseTemplate(False, data=ferricyanide)
    except: 
        return responseTemplate(True, data=None)


@app.post("/balance-stoichiometry")
async def balanceStoichiometry(stoichiometry: Stoichiometry):
    try:
        reac, prod = balance_stoichiometry(stoichiometry.left, stoichiometry.right)
        return responseTemplate(False, data={reac, prod})
    except: 
        return responseTemplate(True, data=None)

