# função para somar dois numeros
def soma(a, b):
    res = a + b
    return res


def soma2(a, b=0):  # define b como 0 a menos que se defina outro valor
    res = a + b
    return res


# Polimorfismo de funções -> aceita mais de um tipo de valor

# soma ("jessica", " silva") => "jessica silva"
# soma ( (2, 3) , (4, 5)) => (2, 3, 4, 5)
# soma (1.5, 1.5) => 3


# programa que calcula fatorial de um numero

def fatorial(n):
    rfat = 1
    for k in range(n, 1, -1):
        rfat = rfat * k
    return rfat


if __name__ == "__main__":  # serve para definir se o programa está sendo executado como programa principal, ou como programa importado
    numero = int(input("Entre com um numero para fatoração: "))
    f = fatorial(numero)

    print("Fatorial de %s: %s" % (numero, f))
