fila = 8
columna = 8
mapa = [
    ["E", "-", "-", "-", "-", "-", "-", "-"],  # E significa Entrada
    ["V", "V", "V", "V", "V", "V", "V", "-"], 
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "V", "V", "V", "V", "V", "V", "V"],  # V significa Vacío
    ["-", "-", "-", "-", "-", "-", "-", "-"],  # - es Vía
    ["V", "V", "V", "V", "V", "V", "V", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["S", "V", "V", "V", "V", "V", "V", "V"],  # S significa Salida
]

Carros = {}

def MostarMapa():
    print("El mapa es: ")
    for fila in mapa:
        print(" ", fila)
    print()

def Espacio():
    for i in range(fila):
        for j in range(columna):
            if mapa[i][j] == "V":
                return (i, j)
    return None

def IngresarVehiculo():
    placa = input("Ingrese la placa del Carro: ")  # Manejado como texto
    if placa in Carros:
        print("El vehículo ya está registrado.")
        return

    espacio = Espacio()
    if espacio:
        i, j = espacio
        mapa[i][j] = "O"  # O significa Ocupado
        hora_ingreso = int(input("Ingrese la hora de entrada del carro en minutos: "))
        Carros[placa] = (i, j, hora_ingreso)
        print(f"Carro con placa {placa} ingresado en la posición ({i},{j}) a los {hora_ingreso} minutos.")
        MostarMapa()
    else:
        print("No hay espacios disponibles.")

def RetirarVehiculo():
    placa = input("Ingrese la placa del carro a retirar: ")
    if placa not in Carros:
        print("Vehículo no encontrado.")
        return

    i, j, hora_entrada = Carros[placa]
    hora_salida = int(input("Ingrese la hora de salida del carro en minutos: "))
    tiempo = hora_salida - hora_entrada

    if tiempo <= 0:
        print("Error: la hora de salida debe ser mayor que la de entrada.")
        return

    tarifa_minuto = 100
    total = tiempo * tarifa_minuto

    mapa[i][j] = "V"  # El espacio queda vacío
    del Carros[placa]

    print(f"Vehículo con placa {placa} retirado.")
    print(f"Tiempo en parqueadero: {tiempo} minutos.")
    print(f"Total a pagar: ${total}")
    MostarMapa()

def MapaActualizado():
    print("Mapa actualizado del parqueadero es:")
    for i in range(fila):
        for j in range(columna):
            print(mapa[i][j], end=" ")
        print()
    print()

def Menu():
    while True:
        print("Menu del super Parqueadero de Miguel y Thomas")
        print("1. Ingresar un vehículo")
        print("2. Retirar un vehículo")
        print("3. Mostrar mapa actualizado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            IngresarVehiculo()
        elif opcion == "2":
            RetirarVehiculo()
        elif opcion == "3":
            MapaActualizado()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

Menu()
