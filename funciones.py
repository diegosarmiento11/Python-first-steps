opcion = int(input('escoge una opción (1, 2, 3): '))


def imprimir_mensaje(mensaje):
    print('Hola')
    print('Cómo estás?')
    print(mensaje)
    print('Adiós')

if opcion == 1:
    imprimir_mensaje('escogiste la opción 1')

elif opcion == 2:
    imprimir_mensaje('escogiste la opción 2')    

elif opcion == 3:
    imprimir_mensaje('escogiste la opción 3')  
else:
    print('escoge la opción correcta')
    
