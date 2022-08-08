import meujogo.base as mjb
import meujogo.player as mjp
import meujogo.jogo as mjj

# mjb.tela('Copa do Mundo', espaco=True)
paises = mjb.selecoes(ordem=False)

mjb.indice(paises)

# player = mjp.player_escolher()
# player = paises[player-1]

mjj.fase_de_grupos(mjb.formatar, paises)
