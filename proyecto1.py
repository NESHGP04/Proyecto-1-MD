'''
=== PROYECTO 1 MATE DISCRETA ===
    Camila Richter 23183
    Marinés García 23391
'''

def obtener_conjunto(vacio): #determinar si el conjunto es vacío
    
    while True:
        entrada = input("Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9), separados por comas (deje vacío para un conjunto vacío): ").upper() #solicita al usuario que ingrese el conjunto deseado, todas las letras la spone en mayúscula
        
        if not entrada.strip(): 
            return set(vacio) #si no ingresa nada, retorna el conjutno es vacío
        
        elementos = [e.strip() for e in entrada.split(",")]
        
        conjunto_valido = {e for e in elementos if e.isalnum() and (len(e) == 1) and (e.isdigit() or 'A' <= e <= 'Z')} #revisa que los números solamente tienen 1 dígito y las letras están de la A a la Z
        
        if len(elementos) == len(conjunto_valido): #verifica que los elementos sean válidos, si no es así devuelve un error
            return conjunto_valido
        else:
            print("Entrada inválida. Solo se permiten letras (A-Z) y dígitos (0-9). Intente de nuevo.")


def ingresar_conjuntos(): #función para ingresar conjuntos
    conjuntos = [] #declara el un array para ingresar todos los conjuntos que el usuario desea
    vacio = "Ø" #declara el conjunto vacío
    while True:
        conjunto = obtener_conjunto(vacio) #si el nuevo conjunto está vacío, no lo agrega al array
        if not conjunto:
            print("Conjunto vacío no se agregará.")
        else:
            conjuntos.append(conjunto) #hace append del nuevo conjunto al array que contiene todos los conjuntos
            print(f"Conjunto {len(conjuntos)} agregado: {conjunto}")
        
        continuar = input("¿Desea ingresar otro conjunto? (s/n): ").lower()
        if continuar != 's': #si el usuario ingresa n, hay un break que detiene esta función
            break
    
    return conjuntos #devuelve el array con todos los conjuntos

def mostrar_conjuntos(conjuntos): 
    print("\nConjuntos ingresados:")
    for i, conjunto in enumerate(conjuntos, start=1): #como cada conjunto es un elemento, usa los índices del array conjuntos para acceder al conjunto estpecífico
        print(f"Conjunto {i}: {conjunto}")

def complemento(conjunto, universo): #utiliza de parámetros el conjunto a evaluar y el conjunto universo
    complemento = [] #crea un array para guardar los elementos del complemento
    
    #revisa si el conjunto es subconjunto del universo, de no ser así no se podría realizar el complemento
    for elemento in conjunto: #verifica si todos los elementos del conjunto están en el universo
        if elemento not in universo: #si los elementos no están en el universo, no es posible realizar el complemento
            return "El conjunto no es un subconjunto del universo."

    for elemento in universo:
        if elemento not in conjunto: #si el elemento está en el universo, pero no en el conjunto, se hace append de ese elemento al array llamado complemento
            complemento.append(elemento)

    return complemento #devuelve el array complemento

def union(conjunto1, conjunto2): #utiliza de parámetros el conjunto 1 a evaluar y sel conjunto 2
    union = set(conjunto1) #agrega a la variable union todos los elementos del conjunto 1
    
    for elemento in conjunto2: 
        if elemento not in union: 
            union.add(elemento) #para cada elemento del conjunto 2 que no está ya en union, lo agrega
    
    return union #devuelve los valores guardados en la variable union


def interseccion(conjunto1, conjunto2): #utiliza de parámetros el conjunto 1 a evaluar y sel conjunto 2
    interseccion = [] #crea un array para guardar los elementos de la intersección
    for elemento in conjunto1:
        if elemento in conjunto2: #busca elementos comunes entre conjunto1 y conjunto2
            interseccion.append(elemento) #hace append de los elementos que pertenecen a ambos conjutnos en el array intersección
    
    return interseccion #devuelve el array intersección

def diferencia(conjunto1, conjunto2): #utiliza de parámetros el conjunto 1 a evaluar y sel conjunto 2
    diferencia = [] #crea un array para guardar los elementos de la diferencia
    for elemento in conjunto1: #busca los elementos del conjunto1 que no están en el conjunto2
        if elemento not in conjunto2:
            diferencia.append(elemento) #hace un append al array diferencia de todos los elementos que cumplen con la condición
    
    return diferencia #devuelve el array diferencia

def difSimetrica(conjunto1, conjunto2): #utiliza de parámetros el conjunto 1 a evaluar y sel conjunto 2
    dif_simetrica = [] #crea un array para guardar los elementos de la diferencia simétrica
    
    for elemento in conjunto1:
        if elemento not in conjunto2: #busca los elementos que están en el conjunto1 pero no en el conjunto2
            dif_simetrica.append(elemento) #hace un append al array diferencia simétrica de todos los elementos que cumplen con la condición
    
    for elemento in conjunto2:
        if elemento not in conjunto1: #busca los elementos que están en el conjunto2 pero no en el conjunto1
            dif_simetrica.append(elemento) #hace un append al array diferencia de todos los elementos que cumplen con la condición
    
    return dif_simetrica #devuelve el array diferencia simétrica


def realizar_operaciones(conjuntos, universo): #utiliza de parámetros el array que contiene todos los conjuntos y el conjunto universo
    while True:
        if len(conjuntos) < 2: #solamente permite realizar operaciones si hay más de dos conjuntos en el array conjuntos
            print("Debe ingresar al menos dos conjuntos para realizar operaciones.")
            break
        
        print("\nSeleccione la operación:\n1. Complemento\n2. Unión\n3. Intersección\n4. Diferencia \n5. Diferencia simétrica")
        operacion = int(input("Ingrese su opción: ")) #el usuario decide que operación desea realizar
        
        if operacion == 1: #complemento
            idx = int(input(f"\nSeleccione el conjunto del cual quiere obtener el complemento (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto
            print("\nComplemento:", complemento(conjuntos[idx], universo)) #usa el conjunto en el índice que el usuario indica, además del universo como parámetros de la función
        
        elif operacion == 2: #unión
            idx1 = int(input(f"\nSeleccione el primer conjunto para la unión (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto 1
            idx2 = int(input(f"Seleccione el segundo conjunto para la unión (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto 2
            print("\nUnión:", union(conjuntos[idx1], conjuntos[idx2])) #usa el conjunto en los índices que el usuario indica como parámetros de la función
        
        elif operacion == 3: #intersección
            idx1 = int(input(f"\nSeleccione el primer conjunto para la intersección (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto 1
            idx2 = int(input(f"Seleccione el segundo conjunto para la intersección (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto 2
            print("\nIntersección:", interseccion(conjuntos[idx1], conjuntos[idx2])) #usa el conjunto en los índices que el usuario indica como parámetros de la función
        
        elif operacion == 4: #diferencia
            idx1 = int(input(f"\nSeleccione el primer conjunto para la diferencia (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto 1
            idx2 = int(input(f"Seleccione el segundo conjunto para la diferencia (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto 2
            print("\nDiferencia:", diferencia(conjuntos[idx1], conjuntos[idx2])) #usa el conjunto en los índices que el usuario indica como parámetros de la función

        elif operacion == 5: #diferencia simétrica
            idx1 = int(input(f"\nSeleccione el primer conjunto para la diferencia simétrica (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto 1
            idx2 = int(input(f"Seleccione el segundo conjunto para la diferencia simétrica (1-{len(conjuntos)}): ")) - 1 #pide al usuario que ingrese el índice del conjunto 2
            print("\nDiferencia Simétrica:", difSimetrica(conjuntos[idx1], conjuntos[idx2])) #usa el conjunto en los índices que el usuario indica como parámetros de la función
        
        else: print("\nOpción de operación no válida") #da error si no ingresa ninguna de las opciones
        
        continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if continuar != 's': #si el usuario ingresa n, hay un break que detiene esta función
            break


print("\n=== PROYECTO 1 MATE DISCRETA ===")

#declaración de variables
salir = True
conjuntos = []
vacio = "Ø"
universo = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)] + [vacio] #declara el conjunto universo del programa, que contiene los números de 1 a 9 y las letras de la A a la Z

print("\nUniverso definido:", universo) #muestra el conjunto universo


while salir:
    
    opc = int(input("\nMENU \n1. Construir conjuntos \n2. Operar conjuntos \n3. Finalizar \nIngrese su opción: ")) #solicita al usuario que ingrese la opción a realizar
    
    if opc == 1: #construir conjuntos
        print("\nConstruir conjuntos")
        conjunto = obtener_conjunto(vacio)
        if conjunto:
            conjuntos.append(conjunto) #agrega el conjunto ingresado al array de conjuntos
            print("Conjunto ingresado:", conjunto)
    
    elif opc == 2: #operaciones
        print("\nOperar conjuntos")
        realizar_operaciones(conjuntos, universo) #llama a la función que contiene todas las operaciones para que usuario decida cuál quiere realizar
    
    elif opc == 3: #salir
        print("\nHa salido del programa!")
        salir = False