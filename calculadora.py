# Función para realizar una suma
def suma(a, b):
    return a + b
# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


# Función principal para la calculadora
def calculadora():
    print("Calculadora básica")
    while True:
        print("Opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Elige una opción (1/2/3/4/5): ")
        
        if opcion == '5':
            break
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Ingresa números válidos.")
            continue

        if opcion == '1':
            resultado = suma(num1, num2)
        elif opcion == '2':
            resultado = resta(num1, num2)
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
        elif opcion == '4':
            resultado = division(num1, num2)
        else:
            print("Opción no válida.")
            continue

        print("Resultado: ", resultado)


calculadora()