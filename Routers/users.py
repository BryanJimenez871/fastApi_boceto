from fastapi import APIRouter, HTTPException
from Schema.users import UsersSchema
from Crud.users import UsersCrud
import logging


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UsersSchema)
async def crear_usuario(user: UsersSchema):
    new_user = user.model_dump(exclude={"id"})
    new_id = await UsersCrud.create_user(new_user)
    logging.basicConfig(level=logging.INFO)
    logging.info(f"{new_user=} {user=}")
    return UsersSchema(**new_user, id=new_id)

@router.get("/", response_model=list[UsersSchema])
async def listar_usuarios():
    tabla = await UsersCrud.select()
    if tabla is None:
        raise HTTPException(status_code=404, detail='No existen registros en la tabla')
    return tabla

@router.get("/{id}", response_model=UsersSchema)
async def obtener_usuario(user_id: int):
    usuario = await UsersCrud.get_user(user_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    return usuario
