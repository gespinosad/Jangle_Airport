import pymysql


def obtener_conexion():
    return pymysql.connect(host='localhost',  # probar con su usuario de sistema o localhost
                                user='root',  # probar con root
                                password='Hinokami2027.',
                                db='jangleairport')
