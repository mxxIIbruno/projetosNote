def tela(msg, espaco=False):
    from time import sleep

    if espaco:
        print(' '*21, end='')

    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.5)

    print()


def selecoes(ordem=None):
    from random import shuffle

    lista = [
        'Catar', 'Equador', 'Senegal', 'Holanda', 'Inglaterra', 'Irã', 'Estados Unidos da America', 'Pais de Gales',
        'Argentina', 'Arábia Saudita', 'México', 'Polônia', 'França', 'Austrália', 'Dinamarca', 'Tunísia',
        'Espanha', 'Costa Rica', 'Alemanha', 'Japão', 'Bélgica', 'Canadá', 'Marrocos', 'Croácia',
        'Brasil', 'Sérvia', 'Suíça', 'Camarões', 'Portugal', 'Gana', 'Uruguai', 'Coreia do Sul'
    ]
    if ordem == 1:
        lista.sort()
    if ordem == 2:
        shuffle(lista)

    return lista


def indice(*args):
    lista = list(*args)
    tamanho = len(lista)

    for x in range(tamanho):
        if x % 8 == 0:
            print()
        print(formatar(lista[x], posicao=x + 1), end=' ')

    print('\n')


def formatar(valor, posicao=None):
    gerar = valor.split()
    novo = posicao

    for juncao in ['da', 'de', 'do']:
        for parte in gerar:
            if parte == juncao:
                gerar.remove(parte)

    if novo is not None:
        novo = f'{novo:>2}-'
    else:
        novo = ''

    if len(gerar) < 2:
        return f'{novo}{gerar[0][:3].upper()}'
    if len(gerar) < 3:
        return f'{novo}{gerar[0][0]+gerar[1][:2].upper()}'
    else:
        return f'{novo}{"".join([x[0] for x in gerar])}'
