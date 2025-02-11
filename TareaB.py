#Enfoque Orientado a Objetos (OO)
from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        divisor = gcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

def main():
    num = int(input("Ingrese el numerador: "))
    den = int(input("Ingrese el denominador: "))

    try:
        fraccion = Fraccion(num, den)
        print(f"La fracción simplificada es: {fraccion}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
