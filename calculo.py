def calculadora():
    while True:
        print("Selecciona la operación que deseas realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingresa el número de la operación: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        try:
            cantidad_numeros = int(input("¿Cuántos números deseas ingresar? "))
            numeros = []
            for i in range(cantidad_numeros):
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)

            if opcion == "1":
                resultado = sum(numeros)
                print("La suma es:", resultado)
            elif opcion == "2":
                resultado = numeros[0]
                for num in numeros[1:]:
                    resultado -= num
                print("La resta es:", resultado)
            elif opcion == "3":
                resultado = 1
                for num in numeros:
                    resultado *= num
                print("La multiplicación es:", resultado)
            elif opcion == "4":
                resultado = numeros[0]
                for num in numeros[1:]:
                    resultado /= num
                print("La división es:", resultado)
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

        except ValueError:
            print("Error: Debes ingresar un número válido.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")

        continuar = input("¿Deseas realizar otra operación? (s/n): ")
        if continuar.lower() != "s":
            print("¡Hasta luego!")
            break

# Llamar a la función para que se ejecute
calculadora()
