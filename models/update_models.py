from pydantic import BaseModel
from datetime import datetime

class UpdateIn(BaseModel):
    username: str
    telefono: int
    email: str

class UpdateOut(BaseModel):
    
    cedula: int
    
    username: str
    nombre: str
    apellido: str
    apellido2: str
    direccion: str
    telefono: int
    email: str
    observaciones: str

class ClienteCreado(BaseModel):
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