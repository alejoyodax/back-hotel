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
    saldo: int

usuarios_db = Dict[int, ClienteInDB]

usuarios_db = {
    "alejoyodax": ClienteInDB(**{
            "cedula":"123456789",
            "contrasena":"asd123",
            "username":"alejoyodax",
            "nombre":"alejandro",
            "apellido":"silva",
            "apellido2":"jaramillo",
            "direccion":"calle falsa 123",
            "telefono":3194212354,
            "email":"alejoyodax@gmail.com",
            "observaciones":"alérgico al agua",
            "saldo":450000}),

    "juanito": ClienteInDB(**{
            "cedula":"12345",
            "contrasena":"asd123",
            "username":"juanito",
            "nombre":"juan",
            "apellido":"asdasd",
            "apellido2":"asdasd",
            "direccion":"calle falsa 999",
            "telefono":1111111111,
            "email":"juanito@gmail.com",
            "observaciones":"muy cansón",
            "saldo":270000})  
}


def get_cliente(username:str):
    if username in usuarios_db.keys():
        return usuarios_db[username]
    else:
        return None


