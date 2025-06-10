import os

## 1. Defino la clase Emprendedor para el primer caso que contiene el precio de la suscripcion, la cantidad de usuarios y el gasto total.
## 2. Dentro defino el metodo calcular_utilidades para el calculo de utilidades con la ecuación dada.
## 3. Defino dos metodos con @staticmethod para llamarlas sin necesidad de instanciar, una es limpiar pantalla
## y el otro para calcular la razon de las utilidades solicitada en el tercer caso.
class Emprendedor:
    def __init__(self, precio_sus: float, usuarios: int, gastos: float):
        self.precio_sus = precio_sus
        self.usuarios = usuarios
        self.gastos = gastos

    def calcular_utilidades(self) -> float:
        utilidades = (self.precio_sus * self.usuarios) - self.gastos
        return utilidades
    
    @staticmethod
    def calcular_razon(utilidad_presente: float, utilidad_anterior: float) -> float:
        razon = utilidad_presente / utilidad_anterior
        return razon
    
    @staticmethod
    def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear")

    

## 1. Defino la clase Emprendedor2 para el segundo caso, heredando los atributos de Emprendedor y añadiendo la cantidad de usuarios premium.
## 2. Aplico polimorfismo modificando la funcion calcular_utilidades tomando en cuenta los usuarios premium.    
class Emprendedor2(Emprendedor):
    def __init__(self, precio_sus: float, usuarios: int, gastos: float, usuarios_premium: int):
        super().__init__(precio_sus, usuarios, gastos)
        self.usuarios_premium = usuarios_premium

    def calcular_utilidades(self) -> float:
        utilidades = ((self.precio_sus * self.usuarios) + ((self.precio_sus * 1.5) * self.usuarios_premium)) - self.gastos
        return utilidades
    


## 1. Defino la clase capturar datos para tomar los datos con input, dependiendo si se elige realizar los calculos con usuarios normales
## o usuarios normales y usuarios premium.
class CapturarDatos:
    def normales(self) -> list:
        while True:
            Emprendedor.limpiar_pantalla()
            try:
                precio = float(input("Ingrese el precio de la suscripción: "))
                usuarios = int(input("Ingrese la cantidad de usuarios: "))
                gastos = float(input("Ingrese el gasto total: "))
                return [precio, usuarios, gastos]

            except ValueError:
                Emprendedor.limpiar_pantalla()
                input("Entrada inválida. Intente de nuevo.\nEnter para continuar")
                continue
    
    def normales_premium(self) -> list:
        while True:
            Emprendedor.limpiar_pantalla()
            try:
                precio = float(input("Ingrese el precio de la suscripción: "))
                usuarios = int(input("Ingrese la cantidad de usuarios normales: "))
                usuarios_premium = int(input("Ingrese la cantidad de usuarios premium: "))
                gastos = float(input("Ingrese el gasto total: "))
                return [precio, usuarios, gastos, usuarios_premium]
            
            except ValueError:
                Emprendedor.limpiar_pantalla()
                input("Entrada inválida. Intente de nuevo.\nEnter para continuar")
                continue



## 1. Defino la clase App que contiene el menú para elegir que calculo se realizará y dependiendo de la elección capturo los datos de entrada
## instanciando CapturarDatos.
class App:
    def __init__(self):
        self.datos = CapturarDatos()

    def run(self):

        utilidades = 0
        razon = 0

        while True:
            Emprendedor.limpiar_pantalla()
            print("""Que necesitas hacer:
                  
1. Calcular utilidades solo con usuarios normales.
2. Calcular utilidades con usuarios normales y usuarios premium.
3. Calcular razon de utilidades con respecto al año anterior.
4. Salir
""")        
            if utilidades != 0:
                print(f"Utilidades calculadas: ${utilidades}")

            if razon != 0:
                print(f"La razon con respecto al año anterior es: {razon}")

            eleccion = input()
            if eleccion not in ["1", "2", "3", "4"]:
                continue

            elif eleccion == "1":
                razon = 0
                datos = self.datos.normales()
                emprendedor = Emprendedor(datos[0], datos[1], datos[2])
                utilidades = emprendedor.calcular_utilidades()

            elif eleccion == "2":
                razon = 0
                datos = self.datos.normales_premium()
                emprendedor = Emprendedor2(datos[0], datos[1], datos[2], datos[3])
                utilidades = emprendedor.calcular_utilidades()
                
            elif eleccion == "3":
                if utilidades != 0:
                    Emprendedor.limpiar_pantalla()
                    anterior = float(input("Ingrese las utilidades del año anterior: "))
                    razon = round((Emprendedor.calcular_razon(utilidades, anterior)), 2)

                else:
                    Emprendedor.limpiar_pantalla()
                    print("Aún no se han calculado utilidades")
                    input("\nEnter para continuar")
                    continue

            elif eleccion == "4":
                Emprendedor.limpiar_pantalla()
                exit()


## Instancio app y ejecuto el metodo run para iniciar el programa
app = App()
app.run()