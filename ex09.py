def gera_combinacoes(n: int):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    lista = list(alfabeto[:n])
    permutacoes("", lista)

def permutacoes(prefixo, restante):
    if len(restante) == 0:
        print(prefixo)
    else:
        for i in range(len(restante)):
            permutacoes(prefixo + restante[i], restante[:i] + restante[i+1:])

gera_combinacoes(4)