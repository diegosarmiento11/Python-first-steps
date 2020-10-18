# pesos = input("¿Cuántos pesos colombianos tienes?: ")
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dólares")

# dolares = input("¿cuántos dólares tienes?: ")
# dolares = float(dolares)
# valor_peso = 0.00026
# pesos = dolares / valor_peso
# pesos = round(pesos, 2)
# pesos = str(pesos)
# print("Tienes $" + pesos + " pesos")


menu = """ 
Bienvenido al conversor de monedas de Diego Sarmiento
Por favor introduzca la moneda que quiera convertir

1. Pesos colombianos
2. Pesos Argentinos
3. Pesos Mexicanos
"""

def operacion(local, valor):
    pesos = input(local)
    pesos = float(pesos)
    valor_dolar = valor 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

opcion = int(input(menu))

if opcion == 1:
    operacion("cuantos pesos colombianos tienes?: ", 3875)

if opcion == 2:
    operacion("cuantos pesos artgentinos tienes?: ", 75)

if opcion == 3:
    operacion("cuantos pesos mexicanos tienes?: ", 24)    


    