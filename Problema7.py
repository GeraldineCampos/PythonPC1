num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Menú con opciones
print("\nElige una opción:")
print("1. Sumar los dos números")
print("2. Restar (el primero menos el segundo)")
print("3. Multiplicar los dos números")

opcion = input("\nIntroduce el número de la opción que deseas: ")

if opcion == '1':
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")
elif opcion == '2':
    resta = num1 - num2
    print(f"La resta de {num1} menos {num2} es: {resta}")
elif opcion == '3':
    multiplicacion = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
else:
    print("Opción inválida. Por favor, elige una opción correcta.")