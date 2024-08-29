precio=0
print("Habitaciones disponibles")

print("1.Habitacion para 4 personas $50")
print("2.Habitacion para 2 personas $30")
print("3.Habitacion para 5 personas con vista al mar $80")
print("4.Habitacion para 5 personas  con frente al mar y con aire acondicionado $120")
#Le pregunta al usuario que  habitacion quiere y segun su decision en la estructura if se le asigna el valor a la variable precio y op 

op=input("Escriba el número de la habitación seleccionada")

if op == "1":
    precio=50
    op="Habitación para 4 personas"

elif op == "2":
    op="Habitación para 2 personas"
    precio=30
elif op=="3":
    op="Habitación para 5 personas con vista al mar"
    precio=80
elif op=="4":
   print("Habitacion para 5 personas  con frente al mar y con aire acondicionado")
   precio=120
#Se le pide datos personales al cliente
cliente=input("Nombre del cliente: ")
telefono=input("Telefono: ")
num_noches=int(input("¿Numeros de noches de estancia?"))
Total_hab=precio*num_noches
#Se le pregunta si quiere un servicio adicional y luego en el if se valida que opcion escogio y se le asignan sus respectivos valores a las variables

servicios_adicc=input("¿Desea alguno de los siguientes servicios adicionales escriba el numero de lo contrario escriba n? \n 1. uso de piscina $10 \n 2. cancha de gol $10 \n 3. Spa $ 20 \n")

if  servicios_adicc == "1":
    prec=10
    Total_hab=precio+10
    
    adicional="Uso de piscina"
elif  servicios_adicc=="2":
    adicional="Cancha de golf"
    prec=10
    Total_hab=precio+prec
elif servicios_adicc=="3":
    prec=20
    adicional="SPA"
    Total_hab=precio+prec
else:
    adicional="Ninguno"

#Se imprime la factura con los detalles y validando que si el cliente solicito algun  servicio adicional se le agregue a la factura

print("Factura electrónica: ")

print("Cliente: ", cliente)
print("Telefono: ", telefono)
print("Habitación: ", op)
print("Precio por noche: $", precio)
print("Servicion adicional:  ", adicional)
if  servicios_adicc!= "Ninguno":
    print("Precio del servicio adicional: $", prec)
print("Total: $", Total_hab)










    