from vehiculo import  Vehiculo, Automovil

#Creación de objeto de la clase Automóvil

#Se crea variable vacia para llenarla después
autos =  []
#Se solicita al usuario cantidad de vehículo a insertar
cant_vehiculos = int(input("Cuántos vehículos desea insertar: "))

#Se usa el bucle for y función range para recorrer información
for c in range(cant_vehiculos):
    print(f"Datos del automóvil {c+1}")
    #Se solicita al usuario características específicas del vehículo
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    nro_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en Km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))
    print("")
    coche = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
    autos.append(coche)

#Se usa la función print para mostrar datos en pantalla"
#Se usa el bucle for para recorrer los objetos y el método enumerate
print("\nImprimiendo por pantalla los Vehículos:")
for c, auto in enumerate(autos):
    print(f"Datos del automóvil {c+1}: ", auto)
    
