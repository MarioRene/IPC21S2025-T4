#Ejemplo para simplificar fracciones paradigma procedural
print("---------PARADIGMA PROCEDURAL----------")



#funcionn que calcula MCD usando el algoritmo de Euclides.
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a




#funcion que simplifica una fracción dividiendo el numerador y el denominador por su MCD
def simplificar_fraccion(numerador, denominador):
    divisor = mcd(numerador, denominador)
    return numerador // divisor, denominador // divisor




 #funcion main
def main():


    # Solicitar al usuario que ingrese la fracción
    numerador = int(input("Ingresa el numerador: "))
    denominador = int(input("Ingresa el denominador: "))
    


    # Simplificar la fracción
    numerador_simplificado, denominador_simplificado = simplificar_fraccion(numerador, denominador)
    


    # Mostrar la fracción simplificada
    print(f"La fracción simplificada es: {numerador_simplificado}/{denominador_simplificado}")




#Lo que hace esto es ejecutar el programa llamando a la funcion main
if __name__ == "__main__":
    main()
