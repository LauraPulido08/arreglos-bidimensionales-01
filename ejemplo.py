# Inicio

# Declaración de la matriz para almacenar notas (3 filas - estudiantes, 4 columnas - notas)
notas = [[0] * 4,
         [0] * 4,
         [0] * 4]  # Matriz 3x4 correctamente inicializada en 0
                    # [[0,0,0,0]
                    # [0,0,0,0]
                    # [0,0,0,0]]

# Declaración del arreglo unidimensional para almacenar los promedios de los estudiantes
promedios = [0] * 3  # Lista de 3 elementos inicializados en 0 (un promedio por estudiante)

# Ingreso de notas por teclado
for estudiante in range(3):  # Recorre las filas (estudiantes)
    #estudiante=0
    #------------
    #estudiante=1
    for nota in range(4):  # Recorre las columnas (notas)
        #nota=0
        #nota=1
        #nota=2
        #nota=3
        #nota=4 ya no cumple el rango entonces se sale del ciclo
        #--------------------------------------------------------
        #nota=0
        # Se usa (nota + 1) y (estudiante + 1) porque los índices inician en 0
        nota_ingresada = input(f"Ingrese la nota {nota + 1} del estudiante {estudiante + 1}: ")
                                #Ingrese la nota 1 del estudiante 1: 10.0
                                #Ingrese la nota 2 del estudiante 1: 9.0
                                #Ingrese la nota 3 del estudiante 1: 7.0
                                #Ingrese la nota 4 del estudiante 1: 10.0
                                #-----------------------------------------
                                #Ingrese la nota 1 del estudiante 2: 10.0
        notas[estudiante][nota] = float(nota_ingresada)  # Conversión a float para manejar decimales
        #10.0 [0][0]
        #9.0 [0][1]
        #7.0 [0][2]
        #10.0 [0][3]
        #------------
        #10.0 [1][0]

# Cálculo del promedio por estudiante y almacenamiento en el arreglo promedios
for estudiante in range(3):  # Recorre las filas (estudiantes)
    #estudiante=0
    #--------------
    #estudiante=1
    suma = 0  # Reinicia el acumulador de suma por cada estudiante
    for nota in range(4):  # Recorre las notas del estudiante
        suma = suma + notas[estudiante][nota]  # Acumulación correcta de notas
        #suma= 0 + 10.0 | 10.0 nota 0
        #suma=10.0 + 9.0 | 19.0 nota 1
        #suma=19.9 + 7.0 | 26.0 nota 2
        #suma=26.0 + 10.0 | 36.0 nota 3
        #-------------------------------
        #suma=0 + 10.0 | 10.0 nota 0
    promedios[estudiante] = suma / 4  # Cálculo correcto del promedio
    #promedios[0]= 36.0/4 = 9.0

# Mostrar los promedios almacenados en el arreglo promedios
print("\nPromedios de los estudiantes:")
contador = 1
for promedio in promedios:
    print(f"El promedio del estudiante {contador} es: {promedio:.2f}")  #  Se imprime con dos decimales
    contador = contador + 1
# Fin
