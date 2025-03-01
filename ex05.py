def F(n:int) -> int:
    if n == 1 or n == 2:
        return n
    return 2 * (F(n-1)) + 3 * (F(n-2))

F(5)