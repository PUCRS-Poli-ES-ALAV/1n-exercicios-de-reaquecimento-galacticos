def somar_div_numeros(numero:int) -> int:
    if numero == 1:
        return 1
    return 1/numero + somar_div_numeros(numero - 1)

somar_div_numeros(4)