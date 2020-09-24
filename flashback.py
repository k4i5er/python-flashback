# Acabus $10
# Taxi casa-escuela $50
# Patín $15

# presupuesto = float(input("Introduce tu presupuesto: "))

# if presupuesto >= 10 and presupuesto < 15:
#     print("Te puedes ir en Acabús")
# elif presupuesto >= 15 and presupuesto < 50:
#     print("Te puedes ir en Acabús o a Patín")
# elif presupuesto >= 50:
#     print("Te puedes ir en Acabús, a Patín o en Taxi")
# else:
#     print("Pídete un ride...")


# Mostrar todos los números enteros pares entre un límite inferior
# y un límite superior

# ¿Qué necesito? Límites sup e inf
limInf = int(input("Escribe el valor para el límite inferior: "))
limSup = int(input("Escribe el valor para el límite superior: "))

# ¿Cómo hago una lista de todos esos números?
# ¿Cómo filtro esa lista para obtener sólo los pares?
num = limInf

while limInf <= num <= limSup:  # num >= limInf and num <= limSup
    if num % 2 == 0:
        print(num)
        num += 2
    else:
        num += 1
