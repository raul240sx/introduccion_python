import os

##  1. Defino la clase Escape la cual construye el objeto con los atributos radio y constante g.
##  2. Contiene el método velocidad_escape que calcula la velocidad de escape con el radio y y la constante g.
##  3. Finalmente contiene la funcion limpiar pantalla con el decorador staticmethod para llamarla sin instaciar.
class Escape:
    def __init__(self, radio: float, constante_g: float):
        self.radio = radio
        self.constante = constante_g
        

    def velocidad_escape(self) -> float:
        ve = (2* self.radio * self.constante) ** 0.5
        ve = round(ve, 1)
        return ve
    
    @staticmethod
    def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear")


## 1. Defino la clase IngresarDatos con el unico método run para capturar los datos con input y un while True
## para evitar los errores de input.
## 2. Finalmente creo el objeto escape con los valores de entrada radio y constante e imprimo el resultado
## de la funcion velocidad_escape
class IngresarDatos:
    def run(self):
        radio = 0
        constante = 0
        
        while True:
            Escape.limpiar_pantalla()
            try:
                radio = float(input("Ingrese el radio en kilómetros: "))
                radio *= 1000
                constante = float(input("Ingrese la constante g en m/s²: "))
                break
            except ValueError:
                Escape.limpiar_pantalla()
                input("Entrada inválida. Intente de nuevo.\nEnter para continuar")
                continue

        escape = Escape(radio, constante)
        resultado = escape.velocidad_escape()
        Escape.limpiar_pantalla()
        print(f"La velocidad de escape es de {resultado} m/s\n")


## Creo la instancia app y ejecuto el metodo app.run() para iniciar el programa
app = IngresarDatos()
app.run()
