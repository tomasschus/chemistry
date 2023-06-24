from pydantic import BaseModel

class Stoichiometry(BaseModel):
    right: object
    left: object
