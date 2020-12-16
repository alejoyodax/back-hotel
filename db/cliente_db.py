from typing import  Dict
from pydantic import BaseModel

class ClienteInDB(BaseModel):
    cedula: int
    contrasena: str
    username: str
    nombre: str
    apellido: str
    apellido2: str
    direccion: str
    telefono: int
    email: str
    observaciones: str

usuarios_db = Dict[int, ClienteInDB]

usuarios_db = {
    "alejo": ClienteInDB(**{
            "cedula":"123456789",
            "contrasena":"12345",
            "username":"alejo",
            "nombre":"alejandro",
            "apellido":"silva",
            "apellido2":"jaramillo",
            "direccion":"calle falsa 123",
            "telefono":33333333,
            "email":"alejoyodax@gmail.com",
            "observaciones":"ninguna"}),

    "juan": ClienteInDB(**{
            "cedula":"12345",
            "contrasena":"12345",
            "username":"juan",
            "nombre":"juan",
            "apellido":"perez",
            "apellido2":"arnoldo",
            "direccion":"calle 23 12a 45",
            "telefono":55555555,
            "email":"juanito@gmail.com",
            "observaciones":"ninguna"}),

    "pepito": ClienteInDB(**{
            "cedula":"123456789",
            "contrasena":"12345",
            "username":"pepito",
            "nombre":"pepe",
            "apellido":"garcía",
            "apellido2":"murcia",
            "direccion":"avenida siempre viva 123",
            "telefono":9999999,
            "email":"pepe@gmail.com",
            "observaciones":"ninguna"})
}

def get_cliente(username:str):
    if username in usuarios_db.keys():
        return usuarios_db[username]
    else:
        return None

