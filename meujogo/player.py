def is_number(valor):
    from re import sub

    return sub(r'[^0-9]', '', valor)


def player_escolher():
    while True:
        entrada = input('Escolha seu pais [índice]: ')
        entrada = is_number(entrada)

        if not entrada.isdigit():
            print('ERRO\n\tEscolha um número.')
            continue

        if not 1 <= int(entrada) <= 32:
            print('Selecione entre 1 e 32 de acordo com o índice.')
            continue

        entrada = int(entrada)

        return entrada
