import sys

from psycopg_pool import AsyncConnectionPool


class Conexion:
    _DATABASE = 'proyecto_api'
    _USERNAME = 'bryan'
    _PASSWORD = 'bryan123456'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    async def obtener_pool(cls):
        if cls._pool is None:
            try:
                # La cadena de conexión suele ser preferible o mediante kwargs
                params = {
                    "dbname": cls._DATABASE,
                    "user": cls._USERNAME,
                    "password": cls._PASSWORD,
                    "host": cls._HOST,
                    "port": cls._DB_PORT
                }
                # Se necesita pasarle un conninfo vació, para que luego lea los kwargs, esto quiere decir:
                # No te voy a pasar una cadena de texto completa (conninfo), mejor mira el diccionario de datos que te paso en kwargs
                cls._pool = AsyncConnectionPool(conninfo="", kwargs=params,
                                           min_size=cls._MIN_CON,
                                           max_size=cls._MAX_CON,
                                           open =False) # Si no pones open=False, el pool intenta abrir conexiones inmediatamente, lo que a veces causa errores si la DB aún no está lista.
                await cls._pool.open()
                return cls._pool
            except Exception as e:
                print(e)
                sys.exit()
        return cls._pool

    @classmethod
    async def cerrar_pool(cls):
        if cls._pool:
            await cls._pool.close()


