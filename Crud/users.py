from Conexiones.Conexion import Conexion
from Schema.users import UsersSchema


class UsersCrud:

    @classmethod
    async def create_user(cls,user: dict):
        sql = """
              INSERT INTO users (name, phone)
              VALUES (%s, %s) 
              RETURNING id;
              """
        pool = await Conexion.obtener_pool()

        async with pool.connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql, (user["name"], user["phone"]))
                user_id = (await cursor.fetchone())[0]
                return user_id

    @classmethod
    async def select(cls):
        sql = 'SELECT * FROM users;'
        pool = await Conexion.obtener_pool()
        async with pool.connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql)
                rows = await cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuario = UsersSchema(id=row[0], name=row[1], phone=row[2])
                    usuarios.append(usuario)
                return usuarios

    @classmethod
    async def get_user(cls,user_id):
        sql = 'SELECT * FROM users WHERE id = %s;'
        pool = await Conexion.obtener_pool()
        async with pool.connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql,(user_id,))
                row = await cursor.fetchone()
                if row is None:
                    return None

                user = UsersSchema(id=row[0], name=row[1], phone=row[2])
                return user
