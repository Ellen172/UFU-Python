#programa que le notas de uma turma e informa quanros alunos ficaram acima da média da turma

def calculaMedia(valores) : 
    return (sum (valores)) / len(valores)

nAlunos = int ( input ("Entre com o numero de alunos: "))

notas = []

for k in range (1, nAlunos+1 ) :
    notaAluno = float ( input ("Entre com a nota do aluno %s: " %(k)) )
    notas.append(notaAluno) #inclui cada nota dada na lista notas

print ("notas: ", notas)

media = calculaMedia(notas) #calcula a media atraves da função calculaMedia
acimaDaMedia = 0

for n in notas : #para todos os elementos em notas, se for maior que a media somasse 1 à acimaDaMedia
    if n>= media :
        acimaDaMedia += 1

print ("Media: ", media)
print ("Quantidade de alunos acima da media: ", acimaDaMedia)