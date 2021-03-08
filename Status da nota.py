#Quarto programa Python
#programa que lê uma nota e informa um status para ela

nota = input("Entre com uma nota: ")
nota = float(nota)

if nota >= 0 and nota <= 5.0 : 
  print("Nota vermelha!")
  print("Você precisa estudar mais...")
#se a nota for maior ou igual a zero e menor ou igual a 5.0, serão executados tudo aquilo após : pela identação

elif 5 <= nota <= 10 :
  print("Nota azul!")
  print("Meus parabéns!")
#senão se a condição do elif for verdade executa os elementos nela identados

else:
  print("Nota invalida.")
#senão executa os elementos identados em else

print("Tenha um bom dia!") #esse comando será impresso independente do if, já que não está igual a identação