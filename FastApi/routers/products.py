from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"message":"No encontrado"}})
# El argumento prefix, es para definirle una ruta ya determinada o por defecto
# Tags es para que separe por tipos de APIS, en la generación de la documentación

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5",]

@router.get('/') # Aqui ya no es necesario poner por argumento '/products' gracias a prefix 
async def products():
    return products_list

@router.get('/{id}') 
async def products(id: int):
    return products_list[id]