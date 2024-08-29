#Ejercicio 2
class PrestamosLibros:
    def __init__(self, libro, nombre, direccion, telefono):
        self.libro = libro
        self.fecha_devolver = None
        self.fecha_prestamo = None
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.sancion = 0

    def prestar(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolver = self.fecha_prestamo + 14

    def devLibro(self, fecha_devolucion):
        if self.fecha_prestamo is None:
            print("El libro no ha sido prestado")
            return

        if fecha_devolucion > self.fecha_devolver:
            self.sancion = (fecha_devolucion - self.fecha_devolver) * 0.35
            print(f"El libro '{self.libro}' tiene sanción de {self.sancion} por entrega tardía.")
        else:
            print(f"El libro '{self.libro}' se devolvió a tiempo")
        self.fecha_prestamo = None
        self.fecha_devolver = None

    def __str__(self):
        return f"{self.nombre} ({self.telefono}), {self.direccion}, {self.libro}, Devolver: {self.fecha_devolver}, Prestamo: {self.fecha_prestamo}"

if __name__ == "__main__":
    print("------Bienvenido al sistema------")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    libro = input("Nombre del libro: ")

    prestamo = PrestamosLibros(libro, nombre, direccion, telefono)

    fecha_prestamo = int(input("Ingresa la fecha de préstamo : "))
    prestamo.prestar(fecha_prestamo)

    print("Fecha de devolución:", prestamo.fecha_devolver)

    fecha_devolucion = int(input("Ingresa la fecha de devolución : "))
    prestamo.devLibro(fecha_devolucion)

    print(prestamo)

    



     
        
