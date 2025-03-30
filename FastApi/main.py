from fastapi import FastAPI # importamos FastApi
from routers import products, users
# pinche entorno virtual
"""
El código asíncrono simplemente significa que el lenguaje 💬 tiene una 
forma de decirle a la computadora / programa 🤖 que en algún 
momento del código, tendrá que esperar que otra cosa termine 
en otro lugar. Digamos que esa otra cosa se llama "archivo-lento" 📝.

técnica de programación que permite que un programa continúe ejecutando 
otras tareas mientras una tarea de larga duración se está ejecutando
"""
app = FastAPI() # Instanciamos FastApi

# ROUTERS
app.include_router(products.router)
app.include_router(users.router)

@app.get('/') # con app nos metemos en el contexto de FastApi
async def root():
    return "Hola FastAPI()"

@app.get('/url') # con app nos metemos en el contexto de FastApi
async def url():
    return { "url_perifl": "https://github.com/SteMt323"}

