#programa que recebe um texto e conta as vogais

texto = input("digite o texto: ")
nvogais = 0

for c in texto :
  if c in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    nvogais += 1

print("numero de vogais: ", nvogais)