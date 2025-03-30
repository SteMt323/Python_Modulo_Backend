from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user", tags=["user"], responses={404: {"message":"No encontrado"}})

# Entidad User
class User(BaseModel):
    id: int
    name: str
    alias: str
    url: str
    age: int
    
users_list = [User(id=1, name="Steven", alias="StvMt323", url="https://github.com/SteMt323", age=18),
              User(id=2, name="Johaneris", alias="johaneris", url="https://github.com/johaneris", age=18)]
    

# OPERACIONES GET d
@router.get('/usersjson') 
async def usersjson():
    return [{"id" : 1, "name" : "Steven", "alias" : "SteMt323", "url" : "https://github.com/SteMt323", "age" : 18},
            {"id" : 1, "name" : "Johaneris", "alias" : "johaneris", "url" : "https://github.com/johaneris", "age" : 18}]

@router.get('/') 
async def users():
    return users_list

# Petición por PATH
@router.get('/{id}') 
async def user(id: int):
    return search_user(id)
    
# Petición por QUERY
@router.get('/', status_code=302) 
async def user(id: int):
    if type(search_user(id)) == User:
        return search_user(id)
    else:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    
   
# OPERACIONES POST
@router.post('/', response_model=User, status_code = 201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario existe")
    # Para lanzar una excepcion "http status code" se usa la palabra reservada "raise"
    else:
        users_list.append(user)
        return user
    

# OPERACIONES PUT s
@router.put('/', status_code=201)
async def user(user: User):
    found = False
    
    for index, save_user in enumerate(users_list):
        if save_user.id == user.id:
            users_list[index] = user
            found = True
        
    if not found:
        raise HTTPException(status_code=304, detail="No se ha modificado el usuario")
    else:
        return user

# OPERACIONES DELETE
@router.delete('/{id}', status_code=201) 
async def user(id: int):   
    found = False
    for index, save_user in enumerate(users_list):
        if save_user.id == id:
            del users_list[index]
            found = True
            
            
    if not found:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
            
    
   
# Función para buscar usuario 
def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return "usuario no encontrado"
    
