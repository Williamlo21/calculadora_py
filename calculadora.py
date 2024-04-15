def sumar(n1, n2):
    print("Resultado de la suma:", n1 + n2)

def restar(n1, n2):
    print("Resultado de la resta:", n1 - n2)

def multiplicar(n1, n2):
    print("Resultado de la multiplicación:", n1 * n2)

def dividir(n1, n2):
    if n2 == 0:
        print("Error: No se puede dividir por cero")
    else:
        print("Resultado de la división:", n1 / n2)

def buscarOperacion(operacion, n1, n2):
    opciones = {
        's': sumar,
        'r': restar,
        'm': multiplicar,
        'd': dividir,
    }
    if operacion in opciones:
        opciones[operacion](float(n1), float(n2))
    else:
        print("Operación no disponible.")
def solicitarnumero():
    n = input()
    nv = validarNumero(n)
    if nv:
        return nv
    
def validarNumero(n):
    try:
        n = float(n)
    except:
        print(str(n) + " no es un número válido")



print("Esta es una calculadora")
print("Por favor indica qué operación deseas realizar.")
print("Escribe 's' si es suma, 'r' si es resta, 'm' si es multiplicación y 'd' si es división:")
operacion = input()
while operacion != 's' and operacion != 'r' and operacion != 'm' and operacion != 'd':
    print("La operación " + operacion + " no está disponible.")
    print("Por favor, indique una operación disponible.")
    operacion = input()



print("Escogiste la opción:", operacion)
print("Ahora digita el primer número para la operación:")
n1 = solicitarnumero()
if n1:
    print("Ahora el segundo número:")
    n2 = solicitarnumero()
    if n2:
        buscarOperacion(operacion, n1, n2)
    