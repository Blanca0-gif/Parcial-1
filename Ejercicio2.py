#Ejercicio 2
class PrestamosLibros:
    def __init__(self, libro, nombre, direccion, telefono):
        #Constructor de la clase
        self.libro = libro
        self.fecha_devolver = None  #Fecha de devolver el libro
        self.fecha_prestamo = None  #fecha de prestamo del libro
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.sancion = 0  #la sancion por entrega retrasada

    def prestar(self, fecha_prestamo):
         #metodo para registrar el libro prestado
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolver = self.fecha_prestamo + 14  # calculo para la fecha de devolución 

    def devLibro(self, fecha_devolucion):
         #metodo para la devolución de un libro
        if self.fecha_prestamo is None:
            print("El libro no ha sido prestado")  # si no hay libro prestado muestra el mensaje
            return

        if fecha_devolucion > self.fecha_devolver:  # si el libro se entrego tarde se sanciona
            self.sancion = (fecha_devolucion - self.fecha_devolver) * 0.35
            print(f"El libro '{self.libro}' tiene sanción de {self.sancion} por entrega tardía.")
        else:
            print(f"El libro '{self.libro}' se devolvió a tiempo")  # si el libro se devolvio a tiempo muestra ese mensaje
        self.fecha_prestamo = None  # se reinicia las fechas hasta el proximo prestamo
        self.fecha_devolver = None
 # metodo para representar el objeto como una cadena
    def __str__(self):
        return f"{self.nombre} ({self.telefono}), {self.direccion}, {self.libro}, Devolver: {self.fecha_devolver}, Prestamo: {self.fecha_prestamo}"

if __name__ == "__main__":  # solicita los datos de info personal y el libro
    print("------Bienvenido al sistema------")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    libro = input("Nombre del libro: ")

     #instancia de la clase
    prestamo = PrestamosLibros(libro, nombre, direccion, telefono)

     #hasta cuando es la fecha de prestamo 
    fecha_prestamo = int(input("Ingresa la fecha de préstamo : "))
    prestamo.prestar(fecha_prestamo)

     #fecha de devolución calculdda del libro
    print("Fecha de devolución:", prestamo.fecha_devolver)

     #solicita la fecha e devolución 
    fecha_devolucion = int(input("Ingresa la fecha de devolución del libro : "))
    prestamo.devLibro(fecha_devolucion)

     #muestra la info del prestamo
    print(prestamo)

    



     
        
