# programa que calcula a combinação de n elementos

import cod  # importa codigo python de um outro arquivo na msm pasta
# o arquivo importado será executado


def combinação(n, p):
    codn = cod.fatorial(n)
    codp = cod.fatorial(p)
    codnp = cod.fatorial(n-p)

    return codn // (codp * codnp)

if __name__ == "__main__":
    a = int ( input ("Entre com a quantidade de elementos: "))
    b = int ( input ("Entre com a quantidade de opções: "))

    comb = combinação(a, b)
    print("A quantidade de combinações possiveis é : ", comb)