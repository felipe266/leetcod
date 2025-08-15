def recurssao_potencia_4(n, m):
    if m == n:
        return True
    elif m > n:
        return False
    else:
        return recurssao_potencia_4(n, m*4)

def potencia_4(n):
    m = 1
    while True:
        if m == n:
            return True
        elif m > n:
            return False
        m *= 4 

n = int(input("digite um numero: "))

print(f"o numero {n} é: {recurssao_potencia_4(n,1)}")