consumo = float(input("¿Cuánto fue su consumo en el restaurante? "))
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar al mesero? "))

propina = consumo * (porcentaje_propina/100)

print(f"La cantidad de dinero que debes dejar como propina es: {propina}")