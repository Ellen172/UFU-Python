#laço de repetição
#programa que pede um numero 'n' ao usuario e imprime os primeiros ns numeros naturais não nulos;

n = input("Entre com o numero: ")
n = int (n)

contador = 1
while contador <= n : 
  print(contador)
  contador = contador + 1 #incrementa o contador em uma unidade

print ("Tenha um bom dia!")