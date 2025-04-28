  # Control de gastos

# Lista de ingresos
lista_de_ingresos = []

# Función para agregar los ingresos    
def agregar_ingresos():
    ingresos = input("Anota aquí tu ingreso y origen(Ej:4500,nomina):  ")
   
    
    # Lo hacemos decimal (float)
    try:
         parte= ingresos.split(",")
         ingreso= parte[0]
         origen=parte[1]
         ingreso = float(parte[0])
        
        # Verificamos que el número sea positivo
         if ingreso <= 0:
            print("Por favor, ingresa un monto positivo.")
         else:
            # Si el número es positivo, lo agregamos a la lista de ingresos
            lista_de_ingresos.append((ingreso,origen))
            print(f"Tu ingreso de {ingreso} por {origen} se ha agregado correctamente.")
    
    except ValueError:
        # Si no es un número válido, mostramos un mensaje de error.
        print("Por favor, agrega un valor positivo.")
    except IndexError:
        print("Por favor, ingresa tanto el monto como el origen, separados por una coma"," ")
        
#lista de gastos
lista_de_gastos= []
#creamos los mismo que hicimos en agresos
def agregar_gastos():
    gastos = input("Anota aquí tu gasto y origen(Ej:4500,nomina):  ")
   
    
    # Lo hacemos decimal (float)
    try:
         parte= gastos.split(",")
         gasto= parte[0]
         origen=parte[1]
         gasto = float(parte[0])
        
        # Verificamos que el número sea positivo
         if gasto <= 0:
            print("Por favor, ingresa un monto positivo.")
         else:
            # Si el número es positivo, lo agregamos a la lista de ingresos
            lista_de_gastos.append((gasto,origen))
            print(f"Tu gasto de {gasto} por {origen} se ha agregado correctamente.")
    except ValueError:
            print("Por favor, ingresa un valor numerico valido para el monto")
    except IndexError:
            print("por favor,ingresa tu monto y origen separados por una "," ")

          
def ver_resumen():
    
    ingresos_totales= sum([ingreso[0] for ingreso in lista_de_ingresos])
    gastos_totales= sum([gasto[0] for gasto in lista_de_gastos])
    sobrante= ingresos_totales-gastos_totales
    
    print (f"Este es tu total de ingresos : {ingresos_totales:.2f}")
    print (f"Este es tu total de gastos: {gastos_totales:.2f}")
    print (f"Este es tu resumen: {sobrante:.2f}") 
    
    if sobrante >0:
        porcentaje_de_sobrante= (sobrante/ingresos_totales)*100
        if porcentaje_de_sobrante >= 30:
            print(f"felicidades!, tienes un sobrante del {porcentaje_de_sobrante:.2f}%.Es excelente,sigue asi!.")
        else:
            print(f"tienes un sobrante del {porcentaje_de_sobrante:.2f}%.Es bueno pero podrias optimizar gastos.")
    elif sobrante <0:
        porcentaje_deficit= abs((sobrante/ingresos_totales)*100)
        print(f"Tu sobrante es negativo:{sobrante:.2f}.Esto significa que tus gastos superan tus ingresos.")
        if porcentaje_deficit >=100:
            print(f"!CUIDADO!, tus gastos superan tus ingresos por mas del 100%. Es crucial que cuides tus salud financiera")
        print("Consejos financieros aqui: [ingresar pagina web] ")
    else:
        print("tus ingresos son iguales a tus gastos")

# Función para mostrar el menú
def mostrar_menu():
    print("\n===== CALCULADORA DE GASTOS =====")
    print("1. Agregar ingreso")
    print("2. Agregar gasto/egreso")
    print("3. Ver resumen")
    print("4. Salir")

# Función principal para ejecutar el programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_ingresos()  # Llamamos a la función para agregar ingreso
        
        elif opcion == "2":
            agregar_gastos()
        
        elif opcion == "3":
            ver_resumen()
        
        elif opcion == "4":
            print("Nos vemos luego, sigue administrando bien tu dinero! :).")
            break
        
        else:
            print("Opción inválida, intenta de nuevo.")
            
            

# Ejecutar el programa
if __name__ == "__main__":
    main()
