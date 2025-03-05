def fibg(n1:int, n2:int, n:int, limite: int) -> None:
    if n == limite:
        return
    if n == 0:
        print(n1)
        fibg(n1, n2, n+1, limite)
        return
    if n == 1:
        print(n2)
        fibg(n1, n2, n+1, limite)
        return
    else: 
        n3 = n1 + n2
        print(n3)
        fibg(n2, n3, n+1, limite) 
        return  

fibg(0,1,0,100)