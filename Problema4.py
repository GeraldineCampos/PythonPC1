Numero = int(input("Ingrese un número entero positivo: "))

if Numero > 0:
    Suma = Numero * (Numero + 1) // 2  
    print(f"La suma de los primeros {Numero} enteros positivos es: {Suma}")
else:
    print("Por favor ingrese un número entero positivo.")
