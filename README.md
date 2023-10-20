# Calculadora Básica

Este es un simple programa de calculadora implementado en Python. La calculadora realiza operaciones de suma, resta, multiplicación y división. Además, proporciona la opción de salir del programa.

## Funciones

### 1. `suma(a, b)`

Esta función toma dos parámetros, `a` y `b`, y devuelve la suma de ambos.

### 2. `resta(a, b)`

Esta función toma dos parámetros, `a` y `b`, y devuelve la resta de `a` menos `b`.

### 3. `multiplicacion(a, b)`

Esta función toma dos parámetros, `a` y `b`, y devuelve el producto de ambos.

### 4. `division(a, b)`

Esta función toma dos parámetros, `a` y `b`, y devuelve el cociente de `a` dividido por `b`. Se incluye una verificación para evitar la división por cero.

### 5. `calculadora()`

Esta es la función principal de la calculadora. Muestra un menú de opciones que permite al usuario elegir entre las operaciones disponibles. También maneja la entrada de números y muestra los resultados de las operaciones.

## Uso

1. Al ejecutar el programa, se mostrará un menú de opciones.
2. El usuario puede elegir una operación ingresando el número correspondiente (1 para suma, 2 para resta, etc.).
3. Se solicita al usuario que ingrese dos números.
4. La operación seleccionada se realiza y se muestra el resultado.
5. El ciclo continúa hasta que el usuario elige salir ingresando '5'.

## Ejecución

Asegúrate de que el nombre de tu archivo principal sea correcto. Actualmente, la condición `if _name_ == "_main_":` tiene un error tipográfico. Debería ser `if __name__ == "__main__":`. Esto asegura que la función `calculadora()` se ejecute solo cuando el script se ejecuta directamente.

```python
if __name__ == "__main__":
    calculadora()
```

Asegúrate de corregir este error para que el programa se ejecute correctamente.