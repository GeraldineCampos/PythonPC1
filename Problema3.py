peso_payaso = 112  
peso_muneca = 75   

num_payasos = int(input("Introduce el número de payasos vendidos: "))
num_munecas = int(input("Introduce el número de muñecas vendidos: "))

peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

print(f"El peso total del paquete es: {peso_total} gramos.")