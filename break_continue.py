def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)

Interrumpiendo ciclo


    for i in range(10000):
        print(i)
        if i == 5768:
            break

    texto = input('Escribre un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()