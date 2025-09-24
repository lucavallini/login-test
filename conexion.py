import pymysql

#Conexion a la base de datos, use pymysql porq mysql.conecctor no me funciono

def getConexion():
    print("DEBUG: Ejecutando getConexion() con PyMySQL...")
    try:
        print("DEBUG: Intentando conectar con PyMySQL...")
        conexion = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='47328448Luca_',
            database='registro_usuarios',
            connect_timeout=5,
            charset='utf8mb4'
        )
        print("DEBUG: Conexión PyMySQL exitosa!")
        return conexion
    except Exception as e:
        print(f"DEBUG: Error PyMySQL: {e}")
        raise e