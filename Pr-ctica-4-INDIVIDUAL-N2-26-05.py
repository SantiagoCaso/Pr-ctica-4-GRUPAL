import sqlite3 



class ProgramaPrincipal:
    def menu(self):
        while True:
            print("Menu de opciones Peluqueria Canina")
            print("1-Cargar perro")
            print("0-Salir del menu")
            nro = int(input("Por favor ingrese un número"))
            if nro == 1:
                nombre_perro = input("Por favor ingrese el nombre del perro: ")
                nombre_dueño = input("Por favor ingrese el nombre del dueño: ")
                domicilio = input("Por favor ingrese el domicilio del perro: ")
                telefono = input("Por favor ingrese el telefono del dueño del perro: ")
                nuevo_perro = Perro(nombre_perro, nombre_dueño, domicilio, telefono)
                nuevo_perro.cargar_perro()
                print("Perro cargado exitosamente")
                self.menu()
            break
        
class Perro:
    def __init__(self, nombre_perro, nombre_dueño, domicilio, telefono):
        self.nombre_perro = nombre_perro
        self.nombre_dueño = nombre_dueño 
        self.domicilio = domicilio
        self.telefono = telefono


    def cargar_perro(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("INSERT INTO PERROS3 VALUES('{}', '{}', '{}', '{}')".format(self.nombre_perro, self.nombre_dueño, self.domicilio, self.telefono))
        conexion.miConexion.commit()
        conexion.cerrarConexion()



class Conexiones:
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria_INDIVIDUAL_N3")
        self.miCursor = self.miConexion.cursor()
    
    def cerrarConexion(self):
        self.miConexion.close()
        

programa = ProgramaPrincipal()
programa.menu()
