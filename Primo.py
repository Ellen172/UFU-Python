#programa que recebe um numero e mostra se ele é primo

n = int (input ("Digite um numero: "))
ndivisores = 0
#conta se há um divisor alem do 1 e ele msm
for k in range (2 , n//2 + 1) : #vai de 2 a n//2 (+1 porque ele se executa ate o ultimo antes de n//2)
#nenhum numero pode ser dividido por outro numero maior que a sua metade
  if n % k == 0 :   #testa se k é divisor de n
    ndivisores += 1 
    break  #interrompe o laço de repetição

if ndivisores == 0 : 
  print("%s é numero primo" %(n))
else : 
  print ("%s não é numero primo" %(n))

