from vehiculo import  Vehiculo, Automovil,  Particular, Carga, Bicicleta, Motocicleta

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta= Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

particular.guardar_datos_cvs()
carga.guardar_datos_cvs()
bicicleta.guardar_datos_cvs()
motocicleta.guardar_datos_cvs()

particular.leer_datos_cvs()
carga.leer_datos_cvs()
bicicleta.leer_datos_cvs()
motocicleta.leer_datos_cvs()