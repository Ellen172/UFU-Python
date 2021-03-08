#função de combinação de n numeros dados p a p

def combinação(n, p):

    def fatorial(a):
        if a == 0:
            return 1
        else:
            return (a * fatorial(a-1))
        
    return fatorial(n) // ( fatorial(p) * fatorial(n-p) )
