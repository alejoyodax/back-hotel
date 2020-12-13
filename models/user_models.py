from pydantic import BaseModel

class ClienteIn(BaseModel):
    username: str
    contrasena: str

class  ClienteOut(BaseModel):
    """
    Esta clase no muestra ciertos datos del cliente, por ejemplo, la contraseña 
    """
    username: str
    nombre: str
    apellido: str
    apellillo2: str

class ClienteOutSaldo(BaseModel):
    username: str
    saldo: int
