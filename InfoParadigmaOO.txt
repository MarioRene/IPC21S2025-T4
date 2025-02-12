#Paradigma OO
##Diagrama de Clases
+------------------------+
|        Fraccion        |
+------------------------+
| - numerador: int  	   |
| - denominador: int	   |
+------------------------+
| + __init__(num, den)   |
| + mcd(a, b): int       |
| + simplificar()        |
| + __str__(): str       |
+------------------------+

Diagrama de Actividades

1.	Inicio
2.	Solicitar al usuario el numerador y denominador
3.	Crear un objeto de la clase Fraccion
4.	Calcular el MCD (Algoritmo de Euclides)
5.	Simplificar la fracción dividiendo numerador y denominador por el MCD
6.	Mostrar la fracción simplificada
7.	Fin

Inicio
│
▼
Solicitar numerador y denominador
│
▼
Crear objeto Fraccion
│
▼
Calcular MCD
│
▼
Simplificar fracción
│
▼
Mostrar fracción simplificada
│
▼
Fin


##Pseudocódigo
INICIO
FUNCION MCD(a, b)
    MIENTRAS b ≠ 0 HACER
        temp ← a
        a ← b
        b ← temp MOD b
    FIN MIENTRAS
    RETORNAR a
FIN FUNCION

CLASE Fraccion
    ATRIBUTOS:
        numerador
        denominador
    METODO __init__(numerador, denominador)
        ASIGNAR numerador A self.numerador
        ASIGNAR denominador A self.denominador
    FIN METODO
    METODO simplificar()
        divisor ← MCD(self.numerador, self.denominador)
        self.numerador ← self.numerador / divisor
        self.denominador ← self.denominador / divisor
    FIN METODO
    METODO __str__()
        RETORNAR self.numerador + "/" + self.denominador
    FIN METODO
FIN CLASE

FUNCION main()
    ESCRIBIR "Ingresa el numerador: "
    LEER numerador
    ESCRIBIR "Ingresa el denominador: "
    LEER denominador
    fraccion ← NUEVO Fraccion(numerador, denominador)
    fraccion.simplificar()
    ESCRIBIR "La fracción simplificada es: " + fraccion
FIN FUNCION

main()
FIN
