def mult_nat(n1, n2):
    if n1 == 1:
        return n2
    return n2 + mult_nat(n1-1,n2)

mult_nat(6,4)