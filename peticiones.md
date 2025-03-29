# Métodos HTTP

El protocolo HTTP (HyperText Transfer Protocol) define varias operaciones que se pueden realizar para interactuar con los recursos en un servidor web. Estas operaciones se corresponden con los **métodos HTTP** que se usan en las solicitudes. A continuación, se detallan los principales métodos HTTP:

## Métodos HTTP

### 1. **GET**
- **Descripción**: Solicita un recurso del servidor.
- **Uso**: Este es el método más común y se utiliza para obtener datos de un servidor (por ejemplo, acceder a una página web).
  
### 2. **POST**
- **Descripción**: Envía datos al servidor para que se procesen.
- **Uso**: Generalmente, se utiliza cuando se desea crear o actualizar un recurso en el servidor (por ejemplo, enviar un formulario).

### 3. **PUT**
- **Descripción**: Sustituye un recurso completo en el servidor con los datos proporcionados en la solicitud.
- **Uso**: Se usa para actualizar recursos existentes en el servidor.

### 4. **DELETE**
- **Descripción**: Elimina un recurso del servidor.
- **Uso**: Se usa para eliminar un archivo o dato en el servidor.

### 5. **PATCH**
- **Descripción**: Realiza una actualización parcial de un recurso en el servidor.
- **Uso**: Similar a PUT, pero solo se modifican los datos específicos indicados, en lugar de reemplazar el recurso completo.

### 6. **HEAD**
- **Descripción**: Solicita un recurso del servidor, pero solo devuelve los encabezados de la respuesta, sin el cuerpo del recurso.
- **Uso**: Se usa cuando solo se necesita obtener los metadatos del recurso (como la longitud del archivo).

### 7. **OPTIONS**
- **Descripción**: Solicita información sobre las opciones de comunicación disponibles para un recurso.
- **Uso**: Se utiliza para verificar los métodos permitidos para un recurso antes de hacer una solicitud.

### 8. **TRACE**
- **Descripción**: Realiza una prueba de diagnóstico, devolviendo la misma solicitud que el servidor recibió.
- **Uso**: Se utiliza para depurar el camino que toma una solicitud a través de los servidores intermediarios.

### 9. **CONNECT**
- **Descripción**: Establece una conexión de túnel con el servidor.
- **Uso**: Se utiliza comúnmente con proxies HTTP para crear un túnel de comunicaciones seguras (como HTTPS).

## Resumen

Los métodos más comunes en las aplicaciones web son:

- **GET**: Obtener recursos.
- **POST**: Enviar datos para crear o actualizar recursos.
- **PUT**: Sustituir recursos completos.
- **DELETE**: Eliminar recursos.
- **PATCH**: Actualizar parcialmente recursos.
