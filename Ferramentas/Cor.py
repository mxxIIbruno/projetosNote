# Fonte
fonte_preto = lambda msg: f'\033[30m{msg}\033[m'
fonte_vermelho = lambda msg: f'\033[31m{msg}\033[m'
fonte_verde = lambda msg: f'\033[32m{msg}\033[m'
fonte_amarelo = lambda msg: f'\033[33m{msg}\033[m'
fonte_roxo = lambda msg: f'\033[34m{msg}\033[m'
fonte_rosa = lambda msg: f'\033[35m{msg}\033[m'
fonte_azul_marinho = lambda msg: f'\033[36m{msg}\033[m'
fonte_cinza = lambda msg: f'\033[37m{msg}\033[m'
fonte_branco = lambda msg: f'\033[38m{msg}\033[m'

# Back
background_black = lambda msg: f'\033[40m{msg}\033[m'
background_red = lambda msg: f'\033[41m{msg}\033[m'
background_green = lambda msg: f'\033[42m{msg}\033[m'
background_yellow = lambda msg: f'\033[43m{msg}\033[m'
background_purple = lambda msg: f'\033[44m{msg}\033[m'
backgorund_pink = lambda msg: f'\033[45m{msg}\033[m'
background_blue = lambda msg: f'\033[46m{msg}\033[m'
background_grey = lambda msg: f'\033[47m{msg}\033[m'
background_white = lambda msg: f'\033[48m{msg}\033[m'


def color(args, func=None, func2=None):
    if func is not None and func2 is not None:
        return func2(func(args))
    elif func2 is not None:
        return func2(args)
    elif func is not None:
        return func(args)
    else:
        return args
