def somar_div_numeros(numero):
    if numero == 1:
        return 1
    return 1/numero + somar_div_numeros(numero - 1)

somar_div_numeros(4)