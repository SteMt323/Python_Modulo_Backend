from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User
class User(BaseModel):
    id: int
    name: str
    alias: str
    url: str
    age: int
    
users_list = [User(id=1, name="Steven", alias="StvMt323", url="https://github.com/SteMt323", age=18),
              User(id=2, name="Johaneris", alias="johaneris", url="https://github.com/johaneris", age=18)]
    

@app.get('/usersjson') 
async def usersjson():
    return [{"name" : "Steven", "alias" : "SteMt323", "url" : "https://github.com/SteMt323", "age" : 18},
            {"name" : "Johaneris", "alias" : "johaneris", "url" : "https://github.com/johaneris", "age" : 18}]

@app.get('/users') 
async def users():
    return users_list

# Petición por PATH
@app.get('/user/{id}') 
async def user(id: int):
    return search_user(id)
    
# Petición por QUERY
@app.get('/user/') 
async def user(id: int):
    return search_user(id)
    
    
def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se ha encontrado al usuario"}