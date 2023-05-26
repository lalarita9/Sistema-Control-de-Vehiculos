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
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} Ruedas "
    
#Clase Automóvil representa un vehículo con velocidad y cilindrada
class Automovil(Vehiculo): 
    
#La clase tiene un constructor __init__ que inicializa los atributos velocidad y cilindrada.
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada): 
        super().__init__(marca, modelo, nro_ruedas) 
        self.velocidad = velocidad
        self.cilindrada= cilindrada
           
    def __str__(self):
        return super().__str__() + f'{self.velocidad} Km/h, {self.cilindrada} cc '

''' Drilling Final
Parte 2:
Partiendo de la descripción anterior por parte del cliente, nos plantea que se manejan dos tipos de 
automóviles tipo: particular y carga, que contienen todas las características de un automóvil.
● Los automóviles tipo particular contienen adicionalmente los números de puesto.
● Los automóviles tipo carga contienen adicionalmente el peso de la carga en kg.
Adicionalmente, se tienen el tipo de vehículos que son bicicleta que contiene las características 
de los vehículos, y se le adiciona el tipo de bicicleta que puede ser: Urbana o de Carrera.
Con los tipos de bicicletas tenemos las motocicletas que contienen todas las características de 
una bicicleta, además de las siguientes: nro_radios, cuadro y motor.
'''
#La clase Particular es la representación de un Automóvil con su atributo número de puesto
class Particular(Automovil): 
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puesto): 
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada) 
        self.nro_puesto = nro_puesto 
    #Método Getters
    def get_nro_puesto(self):
        return self.nro_puesto
    #Método Setters
    def set_nro_puesto(self, nro_puesto2):
        self.nro_puesto = nro_puesto2
     
    def __str__(self):
        return super().__str__() + f'Puestos: {self.nro_puesto}'
    
#La clase Carga es la representación de un Automóvil con su atributo carga   
class Carga(Automovil): 
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga): 
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada) 
        self.carga= carga
            
    def __str__(self):
        return super().__str__() + f'Carga: {self.carga} Kg'
    
#La clase Bicicleta es la representación de un Vehículo con su atributo tipo
class Bicicleta(Vehiculo): 
    def __init__(self, marca, modelo, nro_ruedas, tipo): 
        super().__init__(marca, modelo, nro_ruedas) 
        self.tipo = tipo
            
    def __str__(self):
        return super().__str__() + f'Tipo: {self.tipo}' 

#La clase Motocicleta es la representación de una Bicicleta con su atributo número de radio, cuadro y motor.
class Motocicleta(Bicicleta): 
    #Se cambia el orden de motor y nro para que se imprima en pantalla de acuerdo a instancias dadas      
    def __init__(self, marca, modelo, nro_ruedas, tipo,  motor, cuadro, nro_radio ): 
        super().__init__(marca, modelo, nro_ruedas, tipo) 
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radio= nro_radio
    def __str__(self):
        return super().__str__() + f' Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radio}' 

    
   