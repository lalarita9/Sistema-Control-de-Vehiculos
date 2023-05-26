''' Drilling Final
Parte 1:
● Diseñe el diagrama de clases según los datos capturados con el cliente.
● Partiendo del diseño de diagrama de clases previamente construido, diseñe en las Clases en Python.
● Genere tres instancias, y al ejecutar el programa.
'''
import csv
#Creación de Class Vehículo
class Vehiculo:
    #Constructor
    def __init__(self, marca, modelo, nro_ruedas): 
        self.marca = marca
        self.modelo = modelo 
        self.nro_ruedas = nro_ruedas
      
    #Sobrecarga   
    def __str__(self): 
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} Ruedas, "
    
#Clase Automóvil representa un vehículo con velocidad y cilindrada
class Automovil(Vehiculo): 
    
#La clase tiene un constructor __init__ que inicializa los atributos velocidad y cilindrada.
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada): 
        super().__init__(marca, modelo, nro_ruedas) 
        self.velocidad = velocidad
        self.cilindrada= cilindrada
           
    def __str__(self):
        return super().__str__() + f'{self.velocidad} Km/h, {self.cilindrada} cc '
    
   