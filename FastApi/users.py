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
    

# OPERACIONES GET
@app.get('/usersjson') 
async def usersjson():
    return [{"id" : 1, "name" : "Steven", "alias" : "SteMt323", "url" : "https://github.com/SteMt323", "age" : 18},
            {"id" : 1, "name" : "Johaneris", "alias" : "johaneris", "url" : "https://github.com/johaneris", "age" : 18}]

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
    
   
# OPERACIONES POST
@app.post('/user/')
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario existe"}
    else:
        users_list.append(user)
        return user
    
    
# OPERACIONES PUT
@app.put('/user/')
async def user(user: User):
    found = False
    
    for index, save_user in enumerate(users_list):
        if save_user.id == user.id:
            users_list[index] = user
            found = True
        
    if not found:
        return {"error": "No se ha actualizado al usuario"}
    else:
        return user

   
# Función para buscar usuario 
def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se ha encontrado al usuario"}
    
