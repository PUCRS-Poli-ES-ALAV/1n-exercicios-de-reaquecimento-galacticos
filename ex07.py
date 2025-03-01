def somar_vetor(vetor) -> int:
    if len(vetor) == 1:
        return vetor[0]
    return vetor[-1] + somar_vetor(vetor[:-1])

def mult_vetor(vetor) -> int:
    if len(vetor) == 1:
        return vetor[0]
    return vetor[-1] * mult_vetor(vetor[:-1])

somar_vetor([1,3,4,5])
mult_vetor([3,3,3,10])