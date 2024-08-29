print("Bienvenido a RentCar")
print("¿Qué deseas hacer?")

#le pregunta  al usuario si quiere alquilar un auto o ver los autos disponibles

op=int(print("1. Alquilar un vehículo \n 2.Registrar nuevo vehiculo"))
#si escoge la opcion 1 que es alquilar un auto le pregunta s
if op ==1:
    print("Datos personales")
    nombre=input("Ingrese su nombre:")
    apellido=input("Ingrese su apellido:")
    telefono=input("Ingrese su telefono")
    dias=int(input("ingrese el numero de dias que desea alquilarlo"))
    op2=int(print("¿Qué vehículo deseas alquilar?"))
    print("1.Hyundai Elantra 2019 $25")
    print("2.Honda Civic 2022 $30")
    print("3.Nissan Rogue 2020 $40")
    #Condicional if para asignarle el valor a la variable carro y precioxdia segun su eleccion
    if op2 ==1:
        precioxdia=25
        carro="Hyundai Elantra 2019"
    elif op2 ==2:
        carro="Honda civic 2022"
        precioxdia=30
    elif op2 ==3:
        carro="Nissan  Rogue 2020"

        precioxdia=40
    #Imprime los datos ingresado y calcula el total
    print("Datos de la renta: ")
    print("Nombre:",nombre)
    print("Apellido:",apellido)
    print("Telefono:",telefono)
    print("Vehiculo:",carro)
    print("Precio por dia:",precioxdia)
    print("Total: ", precioxdia*dias)
#Si escoge la segunda opcion de registrar nuevo auto
elif  op ==2:
    print("Datos del vehiculo")
    modeloMarca=input("Ingrese el modelo y la marca")
    año=int(input("Ingrese el año"))
    precio=int(input("Ingrese el precio"))
#Imprime los datos
    print("***Datos guardados**")
    print("Modelo:  ",modeloMarca)
    print("Año: ",año)
    print("Precio: ",precio)


   
    


