#Ejercicio 2

class prestamos_libros:
    
    def__init__(self, libro, nombre, direccion, telefono):
        self.libro = libro
        self.fecha_devolver = None
        self.fecha_prestamo = None
       self.nombre = nombre
       self.direccion = direccion
       self.telefono = telefono
       self.sancion = 0

def prestar(self):
    self.fecha_devolver = self.fecha_prestamo + 14
    self.fecha_prestamo = fecha_prestamo

def devLibro(self, libro_dev):
    if self.fecha_prestamo is None:
        print("El libro no ha sido prestado")
        return

    if libro_dev > self.fecha_devolver:
        self.sancion = (libro_dev - self.fecha_devolver)*0.35
        print("El libro"(self.libro)"tiene sancion de "(self.sancion) "por entrega tardia." )
    else
        print("El libro"(self.libro)"se devolvio a tiempo")
    self.fecha_prestamo = None
    self.fecha_devolver = None

if__name__=="__main__":
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    direccion = input("Direccion: ")

def__str__(self):
    return f"{self.nombre}({self.telefono}),{self.direccion},{self.libro},{self.fecha_devolver},{self.fecha_prestamo}"
    



     
        
