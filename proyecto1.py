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

print("=== PROYECTO 1 ===")

salir = True
while salir:
    opc = int(input("\nMENU \n1. Construir conjuntos \n2. Operar conjuntos \n3.Finalizar \nIngrese su opción: "))
    
    if opc == 1:
        print("\nConstruir conjuntos")
        conjunto = obtener_conjunto()
        print("Conjunto ingresado:", conjunto)

    
    elif opc == 2:
        print("\nOperar conjuntos")
    
    
    elif opc == 3:
        print("\nHa salido del programa!")
        salir = False
    