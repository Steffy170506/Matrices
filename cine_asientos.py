def crear_sala():
    """Crea la matriz de asientos inicial"""
    try:
        filas = int(input("Número de filas de la sala: "))
        columnas = int(input("Número de asientos por fila: "))
        
        if filas <= 0 or columnas <= 0:
            print("Las filas y columnas deben ser mayores a 0. Se usarán valores por defecto (5x5).")
            filas, columnas = 5, 5

        sala = [["L" for _ in range(columnas)] for _ in range(filas)]
        print(f"\nSala creada con {filas} filas y {columnas} asientos por fila.")
        return sala
        
    except ValueError:
        print("Entrada inválida. Se creará una sala de 5x5.")
        return [["L" for _ in range(5)] for _ in range(5)]

def mostrar_sala(sala):
    """Muestra la sala de cine con formato"""
    if not sala:
        print("La sala no ha sido creada.")
        return
    
    filas = len(sala)
    columnas = len(sala[0])
    
    print(f"\n{' SALA DE CINE ':*^40}")
    print(f"Filas: {filas}, Asientos por fila: {columnas}")
    print("*" * 40)

    print("   ", end="")
    for col in range(columnas):
        print(f" {col+1:2} ", end="")
    print()

    for i in range(filas):
        print(f"{i+1:2} ", end="")
        for j in range(columnas):
            if sala[i][j] == "L":
                print(" [L] ", end="")  # Libre
            else:
                print(" [X] ", end="")  # Ocupado
        print()
    
    print("*" * 40)
    print("Leyenda: [L] = Libre, [X] = Ocupado")
    print()

def reservar_asiento(sala):
    """Reserva un asiento si está disponible"""
    if not sala:
        print("La sala no ha sido creada.")
        return sala
    
    try:
        fila = int(input("Número de fila: ")) - 1
        columna = int(input("Número de asiento: ")) - 1
        
        if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
            print("Error: El asiento seleccionado no existe.")
            return sala

        if sala[fila][columna] == "L":
            sala[fila][columna] = "X"
            print(f"¡Asiento reservado exitosamente! (Fila {fila+1}, Asiento {columna+1})")
        else:
            print("Error: El asiento ya está ocupado.")
            
    except ValueError:
        print("Error: Por favor ingrese números válidos.")
    
    return sala

def liberar_asiento(sala):
    """Libera un asiento ocupado"""
    if not sala:
        print("La sala no ha sido creada.")
        return sala
    
    try:
        fila = int(input("Número de fila: ")) - 1
        columna = int(input("Número de asiento: ")) - 1

        if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
            print("Error: El asiento seleccionado no existe.")
            return sala

        if sala[fila][columna] == "X":
            sala[fila][columna] = "L"
            print(f"¡Asiento liberado exitosamente! (Fila {fila+1}, Asiento {columna+1})")
        else:
            print("Error: El asiento ya está libre.")
            
    except ValueError:
        print("Error: Por favor ingrese números válidos.")
    
    return sala

def contar_asientos(sala):
    """Cuenta y muestra estadísticas de asientos"""
    if not sala:
        print("La sala no ha sido creada.")
        return
    
    filas = len(sala)
    columnas = len(sala[0])
    total_asientos = filas * columnas

    libres = 0
    ocupados = 0
    
    for fila in sala:
        for asiento in fila:
            if asiento == "L":
                libres += 1
            else:
                ocupados += 1
    
    print("\n" + "=" * 40)
    print("        ESTADÍSTICAS DE LA SALA")
    print("=" * 40)
    print(f"Total de asientos: {total_asientos}")
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}")
    print(f"Porcentaje de ocupación: {(ocupados/total_asientos)*100:.1f}%")
    print("=" * 40)

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 40)
    print("       SISTEMA DE GESTIÓN DE CINE")
    print("=" * 40)
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")
    print("=" * 40)

def main():
    """Función principal del programa"""
    print("Bienvenido al Sistema de Gestión de Cine")

    sala = crear_sala()
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                mostrar_sala(sala)
            elif opcion == 2:
                sala = reservar_asiento(sala)
            elif opcion == 3:
                sala = liberar_asiento(sala)
            elif opcion == 4:
                contar_asientos(sala)
            elif opcion == 5:
                print("\n¡Gracias por usar el sistema! ¡Hasta pronto!")
                break
            else:
                print("Error: Opción no válida. Por favor seleccione 1-5.")
                
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()