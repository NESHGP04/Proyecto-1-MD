'''
=== PROYECTO 1 MATE DISCRETA ===
    Camila Richter 23183
    Marinés García 23391
'''
def obtener_conjunto():
    while True:
        entrada = input("Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9), separados por comas: ").upper()
        elementos = [e.strip() for e in entrada.split(",")]
        
        # Filtra los elementos válidos
        conjunto_valido = {e for e in elementos if e.isalnum() and (len(e) == 1) and (e.isdigit() or 'A' <= e <= 'Z')}
        
        # Verifica si todos los elementos son válidos
        if len(elementos) == len(conjunto_valido):
            return conjunto_valido
        else:
            print("Entrada inválida. Solo se permiten letras (A-Z) y dígitos (0-9). Intente de nuevo.")

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
    union = conjunto1[:]
    # Agregar los elementos de conjunto2 que no están en conjunto1
    for elemento in conjunto2:
        if elemento not in union:
            union.append(elemento)
    
    return union

def interseccion(conjunto1, conjunto2):
    interseccion = []
    # Buscar elementos comunes entre conjunto1 y conjunto2
    for elemento in conjunto1:
        if elemento in conjunto2:
            interseccion.append(elemento)
    
    return interseccion

print("=== PROYECTO 1 ===")

salir = True
while salir:
    universo = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)]
    print("Universo definido:", universo)

    opc = int(input("\nMENU \n1. Construir conjuntos \n2. Operar conjuntos \n3.Finalizar \nIngrese su opción: "))
    
    if opc == 1:
        print("\nConstruir conjuntos")
        conjuntos = obtener_conjunto()
        print("Conjunto ingresado:", conjuntos)

    
    elif opc == 2:
        print("\nOperar conjuntos")
        if len(conjuntos) < 2:
            print("Debe ingresar al menos dos conjuntos para realizar operaciones.")
        else:
            print("Seleccione la operación:\n1. Complemento\n2. Unión\n3. Intersección")
            operacion = int(input("Ingrese su opción: "))
            
            if operacion == 1:
                idx = int(input(f"Seleccione el conjunto del cual quiere obtener el complemento (1-{len(conjuntos)}): ")) - 1
                print("Complemento:", complemento(conjuntos[idx], universo))
            
            elif operacion == 2:
                idx1 = int(input(f"Seleccione el primer conjunto para la unión (1-{len(conjuntos)}): ")) - 1
                idx2 = int(input(f"Seleccione el segundo conjunto para la unión (1-{len(conjuntos)}): ")) - 1
                print("Unión:", union(conjuntos[idx1], conjuntos[idx2]))
            
            elif operacion == 3:
                idx1 = int(input(f"Seleccione el primer conjunto para la intersección (1-{len(conjuntos)}): ")) - 1
                idx2 = int(input(f"Seleccione el segundo conjunto para la intersección (1-{len(conjuntos)}): ")) - 1
                print("Intersección:", interseccion(conjuntos[idx1], conjuntos[idx2]))
    
    
    
    elif opc == 3:
        print("\nHa salido del programa!")
        salir = False
    