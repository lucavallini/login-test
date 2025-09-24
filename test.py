# test_conexion.py - Ejecuta este archivo separado para probar la conexión
import mysql.connector

def test_mysql_connection():
    print("=== PROBANDO CONEXIÓN MYSQL ===")
    
    try:
        print("1. Intentando conectar SIN especificar base de datos...")
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="47328448Luca_"
        )
        print("✓ Conexión básica exitosa!")
        
        cursor = conexion.cursor()
        print("✓ Cursor creado!")
        
        # Mostrar bases de datos disponibles
        print("\n2. Bases de datos disponibles:")
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        for db in databases:
            print(f"   - {db[0]}")
        
        # Verificar si existe registro_usuarios
        db_exists = any('registro_usuarios' in db for db in databases)
        if db_exists:
            print("✓ Base de datos 'registro_usuarios' existe!")
            
            # Conectar a la base específica
            cursor.execute("USE registro_usuarios")
            print("✓ Conectado a registro_usuarios")
            
            # Mostrar tablas
            print("\n3. Tablas en registro_usuarios:")
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            if tables:
                for table in tables:
                    print(f"   - {table[0]}")
                    
                # Si existe tabla usuarios, mostrar estructura
                table_exists = any('usuarios' in table for table in tables)
                if table_exists:
                    print("\n4. Estructura de tabla 'usuarios':")
                    cursor.execute("DESCRIBE usuarios")
                    columns = cursor.fetchall()
                    for col in columns:
                        print(f"   {col[0]} - {col[1]}")
                else:
                    print("❌ Tabla 'usuarios' NO existe")
            else:
                print("❌ No hay tablas en la base de datos")
                
        else:
            print("❌ Base de datos 'registro_usuarios' NO existe")
            print("\n🔧 SOLUCIÓN: Crear la base de datos:")
            print("CREATE DATABASE registro_usuarios;")
        
        cursor.close()
        conexion.close()
        print("\n✓ Conexión cerrada correctamente")
        
    except mysql.connector.Error as err:
        print(f"❌ ERROR MYSQL: {err}")
        print(f"❌ Código de error: {err.errno}")
        print(f"❌ Descripción: {err.msg}")
        
        if err.errno == 1045:
            print("🔧 SOLUCIÓN: Contraseña incorrecta")
        elif err.errno == 2003:
            print("🔧 SOLUCIÓN: MySQL no está corriendo o puerto bloqueado")
        elif err.errno == 1049:
            print("🔧 SOLUCIÓN: Base de datos no existe")
            
    except Exception as e:
        print(f"❌ ERROR GENERAL: {e}")
        print(f"❌ Tipo: {type(e)}")

if __name__ == "__main__":
    test_mysql_connection()