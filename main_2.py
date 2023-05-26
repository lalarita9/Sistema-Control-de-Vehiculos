from vehiculo import  Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

#Desarrollo de Parte 2
#Creación de objetos a las clases Particular, Carga, Bicicleta y Motocicleta
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta= Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
#Se usa función print para mostrar en pantalla resultados
print("")
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)
print("")

#Verificación de relación entre instancia Bicicleta y otros medios de transporte, usando la función "isinstance"
#Se usa la función print para mostrar el resultado sí la relación es verdadera o falsa
print("Verificación de relación entre instancia Motocicleta y otros medios de transporte")
print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta,Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automóvil: {isinstance(motocicleta,Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta,Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo carga: {isinstance(motocicleta,Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta,Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta,Motocicleta)}")
print("")
