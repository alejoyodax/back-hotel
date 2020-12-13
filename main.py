from db.cliente_db import ClienteInDB, get_cliente
from models.user_models import ClienteIn, ClienteOut, ClienteOutSaldo
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


hotel = FastAPI()


@hotel.get("/") #carpeta raiz del sitio                                        
async def home():   # funcion home asíncrona
    return {"message": "Sistema de reservas hotel"} # muestra un mensaje en la carpeta raiz del sitio

@hotel.post("/user/auth")
async def auth_user(cliente_ingresado: ClienteIn):

    cliente_en_bd = get_cliente(cliente_ingresado.username)
    

    if cliente_en_bd == None:      # si la variable está vacía (quiere decir que user_in_db tambien lo está, porque el usuario al que se intenta acceder no está en la base de datos)
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if cliente_ingresado.contrasena != cliente_en_bd.contrasena:
        return {"Cliente autenticado": False}

    return [{"Autenticado": True}, cliente_en_bd] # si quiero mostrar solo el email y el celular


@hotel.get("/user/saldo/{cliente_ingresado}")
async def get_saldo(cliente_ingresado: str):

    cliente_en_bd = get_cliente(cliente_ingresado)

    if cliente_en_bd == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    cliente_out = ClienteOutSaldo(**cliente_en_bd.dict())

    info_cliente = "INFORMACIÓN DEL CLIENTE : " + str(cliente_en_bd)
    
    return info_cliente, cliente_out


#@hotel.get("/user/")




