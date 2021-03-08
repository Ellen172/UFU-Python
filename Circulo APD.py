#Terceiro programa em Python
#programa que calcula a area, o perimetro e diametro do circulo
#autora: Ellen Christina

raio = input("Entre com o raio do circulo: ")
#a função input recebe apenas elementos Stings, com os quais não conseguimos fazer contas
raio = float(raio) #define que o elemento raio se torna um float
#tambem pode ser usado: raio = float( input("Entre com o raio do circulo: ") )

pi = 3.1415

diametro = 2 * raio #2 vezes raio
perimetro = 2 * pi * raio #2 vezes pi vezes raio
area = pi * (raio ** 2) #pi * (raio elevado a 2)

texto = "Perimetro: %0.2f" %(perimetro)

print("Diametro:", diametro)
print(texto) #dessa forma a variavel texto contem todos os dados e no final só ela precisa ser chamada
print("Area: %0.2f" %(area))
