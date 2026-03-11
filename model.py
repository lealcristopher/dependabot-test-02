from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

def get_user_data():
    user = User(id=1, name="Cristopher")
    return user.dict() # Este método causará um Warning ou erro no futuro