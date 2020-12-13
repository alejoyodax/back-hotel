from pydantic import BaseModel

class ClienteIn(BaseModel):
    username: str
    contrasena: str

class  ClienteOut(BaseModel):
    """
    Esta clase no muestra ciertos datos del cliente, por ejemplo, la contraseña 
    """
    nombre: str
    apellido: str
    apellido2: str
    telefono: int
    email: str

