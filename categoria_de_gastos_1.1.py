# Control de gastos

# Listas globales para ingresos y gastos
lista_de_ingresos = []
lista_de_gastos = []

# Función para ingresar categoría de gasto/ingreso
def ingresar_categoria_de_gastos():
    categorias = {
        "1": "comida",
        "2": "transporte",
        "3": "ocio",
        "4": "ahorro",
        "5": "salud",
        "6": "otros"
    }
    print("Elige una categoría:")
    for clave, valor in categorias.items():
        print(f"{clave}. {valor}")
        
    eleccion = input("Ingresa el número de la categoría: ")
    if eleccion in categorias:
        print(f"Seleccionaste la categoría: {categorias[eleccion]}")
        return categorias[eleccion]
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
        return ingresar_categoria_de_gastos()

# Función para agregar ingresos con categoría
def agregar_ingresos():
    entrada = input("Anota aquí tu ingreso y origen (Ej: 5000, trabajo):  ")
    categoria = ingresar_categoria_de_gastos()
    try:
        parte = entrada.split(",")
        monto = float(parte[0])
        origen = parte[1].strip()
        if monto <= 0:
            print("Por favor, ingresa un monto positivo.")
        else:
            lista_de_ingresos.append((monto, origen, categoria))
            print(f"Tu ingreso de {monto} por '{origen}' en la categoría '{categoria}' se ha agregado correctamente.")
    except ValueError:
        print("Por favor, ingresa un valor numérico válido para el monto.")
    except IndexError:
        print("Por favor, ingresa tu monto y origen separados por una coma ','.")

# Función para agregar gastos con categoría
def agregar_gastos():
    entrada = input("Anota aquí tu gasto y origen (Ej: 4500, nomina):  ")
    categoria = ingresar_categoria_de_gastos()
    try:
        parte = entrada.split(",")
        monto = float(parte[0])
        origen = parte[1].strip()
        if monto <= 0:
            print("Por favor, ingresa un monto positivo.")
        else:
            lista_de_gastos.append((monto, origen, categoria))
            print(f"Tu gasto de {monto} por '{origen}' en la categoría '{categoria}' se ha agregado correctamente.")
    except ValueError:
        print("Por favor, ingresa un valor numérico válido para el monto.")
    except IndexError:
        print("Por favor, ingresa tu monto y origen separados por una coma ','.")

# Función para ver el resumen completo
def ver_resumen():
    total_ingresos = sum([ingreso[0] for ingreso in lista_de_ingresos])
    total_gastos = sum([gasto[0] for gasto in lista_de_gastos])
    
    # Suma de gastos en la categoría "ahorro"
    total_ahorro = sum([gasto[0] for gasto in lista_de_gastos if gasto[2] == "ahorro"])
    
    # Ingresos y gastos por categoría
    resumen_ingresos = {}
    for monto, origen, categoria in lista_de_ingresos:
        resumen_ingresos[categoria] = resumen_ingresos.get(categoria, 0) + monto
    
    resumen_gastos = {}
    for monto, origen, categoria in lista_de_gastos:
        resumen_gastos[categoria] = resumen_gastos.get(categoria, 0) + monto
    
    print("\n=== RESUMEN FINANCIERO ===")
    print(f"Total de ingresos: {total_ingresos:.2f}")
    print(f"Total de gastos:   {total_gastos:.2f}")
    print(f"Total destinado a ahorro: {total_ahorro:.2f}\n")
    
    print("Ingresos por categoría:")
    for cat, tot in resumen_ingresos.items():
        print(f"  {cat}: {tot:.2f}")
    
    print("\nGastos por categoría:")
    for cat, tot in resumen_gastos.items():
        print(f"  {cat}: {tot:.2f}")
    
    balance = total_ingresos - total_gastos
    print(f"\nBalance: {balance:.2f}")
    
    # Mensaje de salud financiera
    if balance > 0:
        pct = (balance / total_ingresos) * 100
        if pct >= 30:
            print(f"¡Felicidades! Tu balance es +{pct:.2f}% de tus ingresos. Excelente gestión.")
        else:
            print(f"Tienes un balance de +{pct:.2f}%. Bien, pero podrías optimizar gastos.")
    elif balance < 0:
        pct = abs((balance / total_ingresos) * 100)
        print(f"Tu balance es negativo ({balance:.2f}), ¡cuidado!")
        if pct >= 100:
            print("¡CUIDADO! Gastas más de lo que ingresas por más del 100%.")
        print("Consejos financieros aquí: [ingresar página web]")
    else:
        print("Tu balance es cero, ingresos iguales a gastos.")

# Función para mostrar el menú
def mostrar_menu():
    print("\n===== CALCULADORA DE GASTOS =====")
    print("1. Agregar ingreso")
    print("2. Agregar gasto/egreso")
    print("3. Ver resumen")
    print("4. Salir")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_ingresos()
        elif opcion == "2":
            agregar_gastos()
        elif opcion == "3":
            ver_resumen()
        elif opcion == "4":
            print("¡Hasta luego! Sigue administrando bien tu dinero 😉")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()

  