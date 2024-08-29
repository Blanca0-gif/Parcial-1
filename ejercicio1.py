print("Bienvenidos al sistema del consultorio San Miguel")


#Se utiliza while para  que el sistema se mantenga en ejecución hasta que el usuario decida salir


while True:
   
    CitaPrevia = input("¿Tiene cita previa? Si (s) o no (n)")
    #se utiliza if para verificar si el usuario cuenta coh cita previa
    if CitaPrevia.lower() == "s":
            print("Paciente pasa a la sala de espera")
    else:
          nombre = input("Ingrese el  nombre del paciente: ")
          

          telefono = input("Ingrese el telefono  del paciente: ")
         

          motivo = input("Ingrese el motivo de visita: ")
         
          fecha=input("Ingrese la fecha de la cita del paciente: ")
          print("********************")
          print("Datos: ")
          print("Paciente: ",nombre)
          print("Telefono: ",telefono)
          print("Motivo de visita: ",motivo)
          print("Fecha de la cita: ",fecha)

          #se le pregunta al usuario si desea hacer otro registro
    nuevoregi=input("¿Desea registrar otro paciente? si (s) o no (n)")
    if nuevoregi.lower() == "n":
          print("Saliendo del sistema")
          
          break
    

