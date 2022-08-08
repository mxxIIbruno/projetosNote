def fase_de_grupos(funcao, *args):
    from itertools import combinations
    from string import ascii_uppercase

    lista = list(*args)
    chaves = {}
    nova_lista = [lista[x: x + 4] for x in range(0, len(lista), 4)]

    for c in ascii_uppercase[:8]:
        chaves[c] = nova_lista[ascii_uppercase.index(c) - 1]

    for definicao_1, definicao_2 in chaves.items():
        print(f'Chave {definicao_1} <- definir')

        for combinacao in combinations(definicao_2, 2):
            valor_1, valor_2 = combinacao
            valor_1, valor_2 = funcao(valor_1), funcao(valor_2)
            print(math(valor_1, valor_2))
            print('=='*8)
        print()


def math(pais_1, pais_2):
    from random import randint
    from time import sleep

    gol_pais_1, gol_pais_2 = 0, 0
    tempo = 0

    while tempo <= 90:
        tempo += 5.4
        if randint(0, 5) % 3 == 0:
            tempo += 3.6
            if randint(0, 6) % 3 == 0:
                gol_pais_1 += 1
                tempo += 4.5
            else:
                gol_pais_2 += 1
                tempo += 4.5
        else:
            tempo += 5

    sleep(0.8)
    return f'\t{pais_1}| {gol_pais_1}\n\t{pais_2}| {gol_pais_2}'
