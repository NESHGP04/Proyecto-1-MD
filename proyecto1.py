'''
=== PROYECTO 1 MATE DISCRETA ===
    Camila Richter 23183
    Marinés García 23391
'''

def obtener_conjunto(vacio):
    

    while True:
        entrada = input("Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9), separados por comas (deje vacío para un conjunto vacío): ").upper()
        
        if not entrada.strip():
            return set(vacio)  # Retornar un conjunto vacío
        
        elementos = [e.strip() for e in entrada.split(",")]
        
        # Filtra los elementos válidos
        conjunto_valido = {e for e in elementos if e.isalnum() and (len(e) == 1) and (e.isdigit() or 'A' <= e <= 'Z')}
        
        # Verifica si todos los elementos son válidos
        if len(elementos) == len(conjunto_valido):
            return conjunto_valido
        else:
            print("Entrada inválida. Solo se permiten letras (A-Z) y dígitos (0-9). Intente de nuevo.")


def ingresar_conjuntos():
    conjuntos = []
    vacio = "Ø"
    while True:
        conjunto = obtener_conjunto(vacio)
        if not conjunto:
            print("Conjunto vacío no se agregará.")
        else:
            conjuntos.append(conjunto)
            print(f"Conjunto {len(conjuntos)} agregado: {conjunto}")
        
        continuar = input("¿Desea ingresar otro conjunto? (s/n): ").lower()
        if continuar != 's':
            break
    
    return conjuntos

def mostrar_conjuntos(conjuntos): #SOLO para ver conjuntos con índice
    print("\nConjuntos ingresados:")
    for i, conjunto in enumerate(conjuntos, start=1):
        print(f"Conjunto {i}: {conjunto}")

def complemento(conjunto, universo):
    complemento = []
    # Verificar si todos los elementos del conjunto están en el universo
    for elemento in conjunto:
        if elemento not in universo:
            return "El conjunto no es un subconjunto del universo."

    # Buscar los elementos del universo que no están en el conjunto
    for elemento in universo:
        if elemento not in conjunto:
            complemento.append(elemento)

    return complemento

def union(conjunto1, conjunto2):
    union = set(conjunto1)
    
    for elemento in conjunto2:
        if elemento not in union:
            union.add(elemento)
    
    return union


def interseccion(conjunto1, conjunto2):
    interseccion = []
    # Buscar elementos comunes entre conjunto1 y conjunto2
    for elemento in conjunto1:
        if elemento in conjunto2:
            interseccion.append(elemento)
    
    return interseccion

def diferencia(conjunto1, conjunto2):
    diferencia = []
    # Agregar elementos de conjunto1 que no están en conjunto2
    for elemento in conjunto1:
        if elemento not in conjunto2:
            diferencia.append(elemento)
    
    return diferencia

def difSimetrica(conjunto1, conjunto2):
    dif_simetrica = []
    
    # Agregar elementos que están en conjunto1 pero no en conjunto2
    for elemento in conjunto1:
        if elemento not in conjunto2:
            dif_simetrica.append(elemento)
    
    # Agregar elementos que están en conjunto2 pero no en conjunto1
    for elemento in conjunto2:
        if elemento not in conjunto1:
            dif_simetrica.append(elemento)
    
    return dif_simetrica


def realizar_operaciones(conjuntos, universo):
    while True:
        if len(conjuntos) < 2:
            print("Debe ingresar al menos dos conjuntos para realizar operaciones.")
            break
        
        print("\nSeleccione la operación:\n1. Complemento\n2. Unión\n3. Intersección\n4. Diferencia \n5. Diferencia simétrica")
        operacion = int(input("Ingrese su opción: "))
        
        if operacion == 1:
            idx = int(input(f"\nSeleccione el conjunto del cual quiere obtener el complemento (1-{len(conjuntos)}): ")) - 1
            print("\nComplemento:", complemento(conjuntos[idx], universo))
        
        elif operacion == 2:
            idx1 = int(input(f"\nSeleccione el primer conjunto para la unión (1-{len(conjuntos)}): ")) - 1
            idx2 = int(input(f"Seleccione el segundo conjunto para la unión (1-{len(conjuntos)}): ")) - 1
            print("\nUnión:", union(conjuntos[idx1], conjuntos[idx2]))
        
        elif operacion == 3:
            idx1 = int(input(f"\nSeleccione el primer conjunto para la intersección (1-{len(conjuntos)}): ")) - 1
            idx2 = int(input(f"Seleccione el segundo conjunto para la intersección (1-{len(conjuntos)}): ")) - 1
            print("\nIntersección:", interseccion(conjuntos[idx1], conjuntos[idx2]))
        
        elif operacion == 4:
            idx1 = int(input(f"\nSeleccione el primer conjunto para la diferencia (1-{len(conjuntos)}): ")) - 1
            idx2 = int(input(f"Seleccione el segundo conjunto para la diferencia (1-{len(conjuntos)}): ")) - 1
            print("\nDiferencia:", diferencia(conjuntos[idx1], conjuntos[idx2]))

        elif operacion == 5:
            idx1 = int(input(f"\nSeleccione el primer conjunto para la diferencia simétrica (1-{len(conjuntos)}): ")) - 1
            idx2 = int(input(f"Seleccione el segundo conjunto para la diferencia simétrica (1-{len(conjuntos)}): ")) - 1
            print("\nDiferencia Simétrica:", difSimetrica(conjuntos[idx1], conjuntos[idx2]))
        
        continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            break


print("\n=== PROYECTO 1 MATE DISCRETA ===")

salir = True
conjuntos = []
vacio = "Ø"
universo = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)] + [vacio]

print("\nUniverso definido:", universo)


while salir:
    

    opc = int(input("\nMENU \n1. Construir conjuntos \n2. Operar conjuntos \n3. Finalizar \nIngrese su opción: "))
    
    if opc == 1:
        print("\nConstruir conjuntos")
        conjunto = obtener_conjunto(vacio)
        if conjunto:
            conjuntos.append(conjunto)
            print("Conjunto ingresado:", conjunto)
    
    elif opc == 2:
        print("\nOperar conjuntos")
        realizar_operaciones(conjuntos, universo)
    
    elif opc == 3:
        print("\nHa salido del programa!")
        salir = False