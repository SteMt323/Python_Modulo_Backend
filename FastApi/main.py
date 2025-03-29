from fastapi import FastAPI # importamos FastApi
"""
El código asíncrono simplemente significa que el lenguaje 💬 tiene una 
forma de decirle a la computadora / programa 🤖 que en algún 
momento del código, tendrá que esperar que otra cosa termine 
en otro lugar. Digamos que esa otra cosa se llama "archivo-lento" 📝.

técnica de programación que permite que un programa continúe ejecutando 
otras tareas mientras una tarea de larga duración se está ejecutando
"""
app = FastAPI() # Instanciamos FastApi

@app.get('/') # con app nos metemos en el contexto de FastApi
async def root():
    return "Hola FastAPI()"

@app.get('/url') # con app nos metemos en el contexto de FastApi
async def url():
    return { "url_perifl": "https://github.com/SteMt323"}

# Generar documentacion: Swagger http://'url_local'/docs
# Generar documentacion: ReDoc http://'url_local'/redoc

"""
OPERACION GET
La operación GET puede referirse a un método de petición HTTP, un 
descriptor de acceso de propiedad o un comando de control de versiones.
 
Método de petición HTTP GET:
- Es el método de petición HTTP más utilizado. 

- Se usa para solicitar información o un recurso específico a un servidor.
 
- Cuando se conecta a un sitio web, el navegador envía peticiones 
  GET para obtener los datos necesarios para cargar la página. 
  
- Las solicitudes GET se pueden almacenar en caché y permanecen 
  en el historial del navegador. 
"""