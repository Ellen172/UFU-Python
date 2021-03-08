#imprimindo os numeros primos, dentro de uma tupla
primos = (1, 3, 5, 7, 11, 13)
for k in primos :
  print(k)

#cria uma tupla de 0 a 5, sem incluir o 5, atraves de uma p.a
r = tuple (range (0, 5)) 
print("r = ", r)

#a tupla é gerada a cada 2 numeros
l = tuple (range (0, 10, 2)) 
print("l =", l)

#cria uma tupla de 0 a 99
for a in range (0, 100) : 
  print(a)

#imprimindo os numeros primos
for k in range(0, len(primos)) :
  print(primos[k]) #k anda nos indices da tupla