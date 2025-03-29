# Backend con Python y FastAPI

Este repositorio contiene un proyecto de backend desarrollado en Python utilizando el framework FastAPI. A continuación, se detallan los pasos para configurar un servidor local con un entorno virtual.

## Configuración del Entorno Virtual

Para levantar el servidor local, se necesita crear y activar un entorno virtual. Sigue los pasos a continuación:

### Paso 1: Crear el entorno virtual

Ejecute el siguiente comando dentro del directorio de su proyecto:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` dentro del directorio donde se ejecutó el comando, que servirá como el entorno virtual.

### Paso 2: Activar el entorno virtual

Dependiendo del sistema operativo y la terminal que estés utilizando, usa uno de los siguientes comandos:

- **PowerShell (Windows):**
  ```powershell
  .\venv\Scripts\Activate
  ```
- **CMD (Windows):**
  ```cmd
  venv\Scripts\activate
  ```

Cuando el entorno virtual esté activado, el prompt de la terminal cambiará para reflejarlo, por ejemplo:

```
(venv) PS C:\Users\username\OneDrive\Desktop\Python-Web>
```

### Paso 3: Instalar las dependencias

Ejecute el siguiente comando para instalar FastAPI y Uvicorn:

```bash
pip install fastapi uvicorn
```

### Paso 4: Verificar la estructura del archivo `main.py`

Asegúrese de que el archivo `main.py` está correctamente estructurado y contiene la configuración necesaria para FastAPI.

### Paso 5: Levantar el servidor con Uvicorn

Ejecute el siguiente comando para iniciar el servidor:

```bash
uvicorn main:app --reload
```

Si el archivo `main.py` está dentro de una subcarpeta, use el siguiente formato:

```bash
uvicorn main_folder.main:app --reload
```

### Paso 6: Verificar que el servidor está corriendo

Si todo se ejecutó correctamente, deberías ver el siguiente output en la terminal:

```
INFO:     Will watch for changes in these directories: ['C:\Users\username\OneDrive\Desktop\Python-Web']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [15752] using StatReload
```

## Nota

Para desactivar el entorno virtual, simplemente ejecute en la terminal:

```bash
deactivate
```

¡Ahora ya puedes trabajar en tu backend con FastAPI! 🚀

