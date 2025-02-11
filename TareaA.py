#Enfoque Procedural
from math import gcd

def solicitar_fraccion():
    num = int(input("Ingrese el numerador: "))
    den = int(input("Ingrese el denominador: "))
    while den == 0:
        print("El denominador no puede ser cero.")
        den = int(input("Ingrese un denominador válido: "))
    return num, den

def simplificar_fraccion(num, den):
    divisor = gcd(num, den)
    return num // divisor, den // divisor

def main():
    num, den = solicitar_fraccion()
    num_simpl, den_simpl = simplificar_fraccion(num, den)
    print(f"La fracción simplificada es: {num_simpl}/{den_simpl}")

if __name__ == "__main__":
    main()
