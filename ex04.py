def pegar_letras(string:str) -> str:
    if len(string) == 1:
        return string
    return string[len(string)-1] + pegar_letras(string[:-1])

pegar_letras('Pedro')