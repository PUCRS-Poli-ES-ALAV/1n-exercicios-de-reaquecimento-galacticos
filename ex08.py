def ver_palindromo(string:str) -> bool:
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return ver_palindromo(string[1:-1])
    return False

ver_palindromo('cbacc')