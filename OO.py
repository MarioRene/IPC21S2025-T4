#Ejemplo para simplificar fracciones paradigma OO
print("---------PARADIGMA OO----------")


#CLASE FRACCION
class Fraccion:
    #instancia de la clase Fraccion usando los valores ingresados por el usuario
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador




  #METODO que calcula MCD usando el algoritmo de Euclides.  
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    



    #METODO que simplifica una fracción dividiendo el numerador y el denominador por su MCD
    def simplificar(self):
        divisor = self.mcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor


    #METODO que devuelve la representación en cadena de la fracción.
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    


#FUNCION principal main
def main():
    # Solicitar al usuario que ingrese la fracción
    numerador = int(input("Ingresa el numerador: "))
    denominador = int(input("Ingresa el denominador: "))
    
    # Crear un objeto Fraccion

    #fraccion es un objeto de la clase Fraccion
    fraccion = Fraccion(numerador, denominador)
    
    # Simplificar la fracción
    fraccion.simplificar()
    
    # Mostrar la fracción simplificada
    print(f"La fracción simplificada es: {fraccion}")




#Lo que hace esto es ejecutar el programa llamando a la funcion main
if __name__ == "__main__":
    main()
