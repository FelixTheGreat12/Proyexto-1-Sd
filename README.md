
# Proyecto 1

## Sistemas distribuidos

### Alumnos:

 - Felipe Martinez Reyna
 - Gerardo Issac Luna Rodarte
 - Cristopher Isaí Velázquez Medina
 - Rodrigo Emiliano Maldonado de la Cruz
 - Rogelio Bustamante Ibarra

# Biblioteca Management API

## Descripción

Este proyecto es una API de gestión de una biblioteca utilizando `FastAPI` y `odmantic`, que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para los siguientes modelos:

- **Autores**
- **Bibliotecarios**
- **Lectores**
- **Libros**
- **Préstamos**

Además, se incluye la funcionalidad de subir y eliminar archivos a un bucket S3 para almacenar imágenes de portadas de libros y fotos de credenciales de lectores.


## Uso

A continuación se describen las operaciones CRUD para cada uno de los modelos:


#### Descripción

Este proyecto proporciona una serie de funciones asíncronas para gestionar autores en una base de datos MongoDB utilizando `odmantic` como ODM (Object-Document Mapper). Permite crear, leer, actualizar y eliminar (CRUD) autores.

### Autores
- **Obtener Todos los Autores**

    ```python
    autores = await get_all_authors(engine)
    ```

- **Obtener un Autor por ID**

    ```python
    author_id = "6476a8f2d3b9c2312b47e3e8"
    autor = await get_author(author_id, engine)

    ```
- **Obtener un Autor por ID**

    ```python
    author_id = "6476a8f2d3b9c2312b47e3e8"
    author_data = Autor(nombre="Gabriel", apellido="García Márquez", biografia="Biografía actualizada.")
    autor_actualizado = await update_author(author_id, author_data, engine)
    ```


- **Eliminar un Autor**

    ```python
    author_id = "6476a8f2d3b9c2312b47e3e8"
    autor_eliminado = await delete_autor(author_id, engine)
    ```
### Bibliotecarios

- **Crear un Bibliotecario**:

    ```python
    from models.bibliotecario import Bibliotecario

    bibliotecario = Bibliotecario(nombre="Ana", apellido="Pérez",  correo="ana.perez@example.com")
    await create_librarian(bibliotecario, engine)
    ```

- **Obtener Todos los Bibliotecarios**:

    ```python
    bibliotecarios = await get_all_librarians(engine)
    ```

- **Actualizar un Bibliotecario**:

    ```python
    updated_data = Bibliotecario(nombre="Ana", apellido="Pérez", correo="ana.perez@newmail.com")
    await update_librarian(librarian_id="6476a8f2d3b9c2312b47e3e8", librarian_data=updated_data, engine=engine)
    ```

- **Eliminar un Bibliotecario**:

    ```python
    await delete_librarian(librarian_id="6476a8f2d3b9c2312b47e3e8", engine=engine)
    ```

### Lectores

- **Crear un Lector**:

    ```python
    from models.lector import Lector

    lector = Lector(nombre="Juan", apellido="Lopez", correo="juan.lopez@example.com")
    await create_reader(lector, engine)
    ```

- **Obtener Todos los Lectores**:

    ```python
    lectores = await get_all_readers(engine)
    ```

- **Actualizar un Lector**:

    ```python
    updated_reader = Lector(nombre="Juan", apellido="Lopez", correo="juan.lopez@newmail.com")
    await update_reader(reader_id="6476a8f2d3b9c2312b47e3e8", reader_data=updated_reader, engine=engine)
    ```

- **Eliminar un Lector**:

    ```python
    await delete_reader(reader_id="6476a8f2d3b9c2312b47e3e8", engine=engine)
    ```

### Libros

- **Crear un Libro**:

    ```python
    from models.libro import Libro
    from fastapi import UploadFile

    await create_libro(
        titulo="Cien Años de Soledad",
        autor_id="6476a8f2d3b9c2312b47e3e8",
        descripcion="Una obra maestra de la literatura.",
        inventario=5,
        archivo=UploadFile(...),  # Archivo de la imagen de la portada
        engine=engine
    )
    ```

- **Obtener Todos los Libros**:

    ```python
    libros = await get_all_libros(engine)
    ```

- **Actualizar un Libro**:

    ```python
    await update_libro(
        libro_id="6476a8f2d3b9c2312b47e3e8",
        titulo="Cien Años de Soledad - Edición Revisada",
        autor_id="6476a8f2d3b9c2312b47e3e8",
        descripcion="Edición especial revisada.",
        inventario=3,
        archivo=UploadFile(...),  # Archivo de la nueva portada (opcional)
        engine=engine
    )
    ```

- **Eliminar un Libro**:

    ```python
    await delete_libro(libro_id="6476a8f2d3b9c2312b47e3e8", engine=engine)
    ```

### Préstamos

- **Crear un Préstamo**:

    ```python
    from datetime import datetime
    from fastapi import UploadFile

    await create_loan(
        lector_id="6476a8f2d3b9c2312b47e3e8",
        libro_id="6476a8f2d3b9c2312b47e3e8",
        fecha_prestamo=datetime.now(),
        bibliotecario_id="6476a8f2d3b9c2312b47e3e8",
        archivo=UploadFile(...),  # Archivo de la foto de credencial
        engine=engine
    )
    ```

- **Obtener Todos los Préstamos**:

    ```python
    prestamos = await get_all_loans(engine)
    ```

- **Actualizar un Préstamo**:

    ```python
    await update_loan(
        prestamo_id="6476a8f2d3b9c2312b47e3e8",
        lector_id="6476a8f2d3b9c2312b47e3e8",
        libro_id="6476a8f2d3b9c2312b47e3e8",
        fecha_prestamo=datetime.now(),
        bibliotecario_id="6476a8f2d3b9c2312b47e3e8",
        archivo=UploadFile(...),  # Archivo de la nueva foto de credencial (opcional)
        engine=engine
    )
    ```

- **Eliminar un Préstamo**:

    ```python
    await delete_loan(prestamo_id="6476a8f2d3b9c2312b47e3e8", engine=engine)
    ```

## Dependencias

- `odmantic`: Un Object-Document Mapper (ODM) para MongoDB.
- `fastapi`: Framework para construir APIs rápidas en Python.
- `motor`: Driver asíncrono de MongoDB para Python.
- `boto3` (opcional): Para la interacción con AWS S3 si se utiliza almacenamiento de archivos.

Asegúrate de incluir estas dependencias en tu archivo `requirements.txt`:

```txt
odmantic
fastapi
motor
boto3
```

# Configuración de Conexión a MongoDB para Biblioteca

## Descripción

Este módulo configura la conexión a una base de datos MongoDB utilizando `odmantic` y `motor`. Permite la conexión asíncrona a una base de datos MongoDB para realizar operaciones CRUD en un sistema de gestión de una biblioteca. 

Se utiliza `pydantic` para la gestión de la configuración, lo que facilita el manejo de variables de entorno para ajustar la URI de conexión y el nombre de la base de datos.

1. Asegúrate de tener un servidor de MongoDB ejecutándose, ya sea localmente o mediante un servicio en la nube como MongoDB Atlas.

## Uso

### Conectar a la Base de Datos

Para conectar a la base de datos, simplemente importa y utiliza la función `connect_db`:

```python
from database import connect_db

await connect_db()
```

- **Cerrar la Conexión**:

    ```python
    await delete_loan(prestamo_id="6476a8f2d3b9c2312b47e3e8", engine=engine)
    ```

- **Crear un Autor**:

    ```python
    from models.autor import Autor
    from database import engine

    autor = Autor(nombre="Gabriel", apellido="García Márquez", biografia="Autor colombiano conocido por Cien Años de Soledad.")
    await create_author(autor, engine)

    ```

- **Obtener Todos los Autores**:

    ```python
    from database import engine

    autores = await get_all_authors(engine)
    print(autores)

- **Obtener un Autor por ID**:

    ```python
    from database import engine

    author_id = "6476a8f2d3b9c2312b47e3e8"
    autor = await get_author(author_id, engine)
    print(autor))
   
- **Actualizar un Autor**:

    ```python
    from models.autor import Autor
    from database import engine

    author_id = "6476a8f2d3b9c2312b47e3e8"
    author_data = Autor(nombre="Gabriel", apellido="García Márquez", biografia="Biografía actualizada.")
    autor_actualizado = await update_author(author_id, author_data, engine)
    print(autor_actualizado)
    ```

- **Eliminar un Autor**:

    ```python
    from database import engine

    author_id = "6476a8f2d3b9c2312b47e3e8"
    autor_eliminado = await delete_autor(author_id, engine)
    print(autor_eliminado)
    ```

## Configuración

La configuración se gestiona a través de la clase `Settings` de `pydantic`. Las variables de entorno pueden configurarse para ajustar la conexión a la base de datos:


- **MONGODB_URI:** URI de conexión a MongoDB. Por defecto: `mongodb://localhost:27017`
- **DATABASE_NAME:** Nombre de la base de datos que se utilizará. Por defecto: `BIBLIOTECA`

# Gestión de Archivos en Amazon S3 para Biblioteca

## Descripción

Este módulo proporciona funciones para subir y eliminar archivos en Amazon S3, utilizando `boto3` y `FastAPI`. Es ideal para manejar archivos como imágenes de portadas de libros, fotos de credenciales, u otros archivos necesarios en un sistema de gestión de una biblioteca.

### Subir un Archivo a S3

La función `upload_file` permite subir un archivo a un bucket de S3 y obtener una URL pública para acceder al archivo. A continuación, un ejemplo de uso:

```python
from fastapi import UploadFile

# Suponiendo que 'file' es un objeto de tipo UploadFile recibido en un endpoint de FastAPI
bucket_name = "tu-bucket"
path = "libros"

file_url_response = await upload_file(file, bucket_name, path)

if "url" in file_url_response:
    print(f"Archivo subido con éxito. URL: {file_url_response['url']}")
else:
    print("Error al subir el archivo.")

```

## Configuración

Para utilizar estas funciones, debes tener configuradas tus credenciales de AWS. Las credenciales pueden configurarse de varias maneras, por ejemplo, utilizando un archivo `~/.aws/credentials` o configurando las variables de entorno:

```env
AWS_ACCESS_KEY_ID=tu_access_key
AWS_SECRET_ACCESS_KEY=tu_secret_key
AWS_REGION=tu_region 
MONGODB_URI=mongodb://localhost:27017/BIBLIOTECA
```
Asegúrate de tener un bucket de S3 creado y de ajustar las configuraciones de nombre del bucket y las rutas utilizadas en las funciones.

## Dependencias

- `fastapi`: Framework para construir APIs rápidas en Python.
- `uvicorn`: Para correr la aplicación de FastAPI (si es necesario para probar localmente).
- `boto3` (opcional): Para la interacción con AWS S3 si se utiliza almacenamiento de archivos.


# Biblioteca API

## Descripción

Este proyecto es una API RESTful desarrollada con `FastAPI` para gestionar una biblioteca. La API permite realizar operaciones CRUD para gestionar:

- **Autores**
- **Bibliotecarios**
- **Lectores**
- **Libros**
- **Préstamos**


### Autores

- **Agregar un Autor**:

    ```python
    POST /autores/
    {
        "nombre": "Gabriel",
        "apellido": "García Márquez",
        "biografia": "Autor colombiano conocido por Cien Años de Soledad."
    }
    ```

- **Obtener Todos los Autores**:

    ```python
    GET /autores
    ```

- **Obtener un Autor por ID**:

    ```python
    GET /autores/{author_id}
    ```

- **Actualizar un Autor**:

    ```python
    PUT /autores/{author_id}
    {
        "nombre": "Gabriel",
        "apellido": "García Márquez",
        "biografia": "Biografía actualizada."
    }
    ```

- **Eliminar un Autor**:

    ```python
    DELETE /autores/{author_id}
    ```

### Bibliotecarios

- **Agregar un Bibliotecario**:

    ```python
    POST /bibliotecarios/
    {
        "nombre": "Ana",
        "apellido": "Pérez",
        "correo": "ana.perez@example.com"
    }
    ```

- **Obtener Todos los Bibliotecarios**:

    ```python
    GET /bibliotecarios
    ```

- **Obtener un Bibliotecario por ID**:

    ```python
    GET /bibliotecarios/{librarian_id}
    ```

- **Actualizar un Bibliotecario**:

    ```python
    PUT /bibliotecarios/{librarian_id}
    {
        "nombre": "Ana",
        "apellido": "Pérez",
        "correo": "ana.perez@newmail.com"
    }
    ```

- **Eliminar un Bibliotecario**:

    ```python
    DELETE /bibliotecarios/{librarian_id}
    ```

### Lectores

- **Agregar un Lector**:

    ```python
    POST /lectores/
    {
        "nombre": "Juan",
        "apellido": "Lopez",
        "correo": "juan.lopez@example.com"
    }
    ```

- **Obtener Todos los Lectores**:

    ```python
    GET /lectores
    ```

- **Obtener un Lector por ID**:

    ```python
    GET /lectores/{reader_id}
    ```

- **Actualizar un Lector**:

    ```python
    PUT /lectores/{reader_id}
    {
        "nombre": "Juan",
        "apellido": "Lopez",
        "correo": "juan.lopez@newmail.com"
    }
    ```

- **Eliminar un Lector**:

    ```python
    DELETE /lectores/{reader_id}
    ```

### Libros

- **Agregar un Libro**:

    ```python
    POST /libros/
    Form Data:
    {
        "titulo": "Cien Años de Soledad",
        "autor_id": "6476a8f2d3b9c2312b47e3e8",
        "descripcion": "Una obra maestra de la literatura.",
        "inventario": 5,
        "archivo": <Archivo de la imagen de la portada>
    }
    ```

- **Obtener Todos los Libros**:

    ```python
    GET /libros
    ```

- **Obtener un Libro por ID**:

    ```python
    GET /libros/{libro_id}
    ```

- **Actualizar un Libro**:

    ```python
    PUT /libros/{libro_id}
    Form Data:
    {
        "titulo": "Cien Años de Soledad - Edición Revisada",
        "autor_id": "6476a8f2d3b9c2312b47e3e8",
        "descripcion": "Edición especial revisada.",
        "inventario": 3,
        "archivo": <Nuevo archivo de la imagen de la portada (opcional)>
    }
    ```

- **Eliminar un Libro**:

    ```python
    DELETE /libros/{libro_id}
    ```

### Préstamos

- **Agregar un Préstamo**:

    ```python
    POST /prestamos/
    Form Data:
    {
        "lector_id": "6476a8f2d3b9c2312b47e3e8",
        "libro_id": "6476a8f2d3b9c2312b47e3e8",
        "fecha_prestamo": "2024-10-27T14:00:00",
        "bibliotecario_id": "6476a8f2d3b9c2312b47e3e8",
        "archivo": <Archivo de la foto de credencial>
    }
    ```

- **Obtener Todos los Préstamos**:

    ```python
    GET /prestamos
    ```

- **Obtener un Préstamo por ID**:

    ```python
    GET /prestamos/{loan_id}
    ```

- **Actualizar un Préstamo**:

    ```python
    PUT /prestamos/{prestamo_id}
    Form Data:
    {
        "lector_id": "6476a8f2d3b9c2312b47e3e8",
        "libro_id": "6476a8f2d3b9c2312b47e3e8",
        "fecha_prestamo": "2024-10-27T14:00:00",
        "bibliotecario_id": "6476a8f2d3b9c2312b47e3e8",
        "archivo": <Nuevo archivo de la foto de credencial (opcional)>
    }
    ```

- **Eliminar un Préstamo**:

    ```python
    DELETE /prestamos/{prestamo_id}
    ```

### Pruebas

  - **Prueba al momento de crear un POST**

    ![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/post.jpg)

  - **Prueba al momento de crear un GET obtener resultado por ID**
    ![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/get.jpeg)
  - **Prueba al momento de crear un GET obtener todos los resultados**
    ![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/getall.jpeg)
  - **Prueba al momento de crear un PUT**
    ![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/put.jpeg)
  - **Prueba al momento de crear un DELETE**
    ![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/delete.jpeg)

### Prueba en MongoDB

- **Autores registrados**
    ![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/mongodb1.jpeg)
- **Bibliotecario registrados**
    ![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/mongodb2.jpeg)
- **Lectores registrados**
    ![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/mongodb3.jpeg)

### Prueba en AWS
- **Biblioteca guardado en AWS**
![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/aws1.jpeg)
- **Imagenes guardado en AWS**
![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/aws2.jpeg)
- **Libros guardado en AWS**
![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/aws3.jpeg)
- **Prestamo guardado en AWS**
![](https://github.com/FelixTheGreat12/Proyexto-1-Sd/blob/main/aws4.jpeg)


