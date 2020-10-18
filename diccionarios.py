def run():
    mi_diccionario = {
        'llave 1': 1,
        'llave 2': 2,
        'llave 3': 3,
        'llave 4': 4,
    }
    print(mi_diccionario['llave 1'])

    poblacion_paises = {
        'argentina': 44,
        'colombia': 50,
        'brasil': 210,
    }

    print(poblacion_paises['argentina'])

    for pais in poblacion_paises.keys():
        print(pais)

    for pais in poblacion_paises.values():
        print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()