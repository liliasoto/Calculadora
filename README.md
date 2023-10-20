# Calculadora Básica en Python

Este es un programa simple de calculadora implementado en Python. La calculadora realiza operaciones de suma, resta, multiplicación y división. También, proporciona la opción de salir del programa.

## Funciones

La aplicación contiene las siguientes funciones:

### 1. `suma(a, b)`

Realiza la suma de dos números, `a` y `b`, y devuelve el resultado.

### 2. `resta(a, b)`

Realiza la resta de `a` menos `b` y devuelve el resultado.

### 3. `multiplicacion(a, b)`

Realiza la multiplicación de dos números, `a` y `b`, y devuelve el resultado.

### 4. `division(a, b)`

Realiza la división de `a` por `b`, asegurándose de evitar la división por cero. Devuelve el cociente o un mensaje de error en caso de división por cero.

## Uso

1. Al ejecutar el programa, se mostrará un menú de opciones.
2. El usuario puede elegir una operación ingresando el número correspondiente (1 para suma, 2 para resta, 3 para multiplicación, 4 para división y 5 para salir).
3. Se solicita al usuario que ingrese dos números.
4. La operación seleccionada se realiza y se muestra el resultado.
5. El ciclo continúa hasta que el usuario elige salir ingresando '5'.

## Ejecución

Para ejecutar esta calculadora básica en tu sistema, simplemente sigue estos pasos:

1. Asegúrate de tener Docker instalado en tu sistema.

2. Abre una terminal y navega al directorio donde se encuentra tu archivo `Dockerfile` y `calculadora.py`.

3. Ejecuta el siguiente comando para construir la imagen de Docker (asegúrate de estar en el directorio correcto):

```bash
docker build -t calculadora-app .
```
4. Una vez que la imagen se haya construido con éxito, puedes ejecutar un contenedor basado en esa imagen utilizando el siguiente comando:

```bash
docker run -it --rm calculadora-app
```
Esto ejecutará tu calculadora Python en el contenedor Docker y mostrará el menú de opciones.

¡Disfruta usando esta calculadora básica en Python! Si tienes alguna pregunta o encuentras algún problema, no dudes en contactar al desarrollador.

