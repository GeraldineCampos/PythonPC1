hora = input("Ingrese la hora en formato 24 horas (ejemplo 7:30 o 12:45): ")

horas, minutos = map(int, hora.split(":"))

hora_decimal = horas + minutos / 60

if 7 <= hora_decimal <= 8:
    print("Es la hora del desayuno.")
elif 12 <= hora_decimal <= 13:
    print("Es la hora del almuerzo.")
elif 18 <= hora_decimal <= 19:
    print("Es la hora de la cena.")