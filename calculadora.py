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


if _name_ == "_main_":
    calculadora()