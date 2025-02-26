def soma_nat(n1,n2):
    if n1 >= 1:
        return 1 + soma_nat(n1-1, n2)
    if n1 == 0 and n2 >= 1:
        return 1+soma_nat(n1,n2-1)
    if n1 == 0 and n2 == 0:
        return 0
    
soma_nat(1,6)