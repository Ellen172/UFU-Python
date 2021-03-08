#programa que calcula media de um determinado grupo de valores

n = int (input ("Escreve a quantidade de elementos: "))
soma = 0

for k in range (1, n+1) : #o for anda em uma sequencia pré existente, impedindo um laço infinito
  valor = float(input ("Entre com o valor %d: " %(k)))
  soma += valor

print("soma dos valores: ", soma)
media = soma/n
print("media dos valores:  %0.2f" %(media))