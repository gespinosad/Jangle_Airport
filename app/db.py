import pymysql


def obtener_conexion():
    return pymysql.connect(host='JEYSON',#probar con su usuario de sistema o localhost
                                user='admin',#probar con root
                                password='3535',
                                db='usuarios')

