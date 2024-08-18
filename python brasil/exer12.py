idades=[]
alturas=[]

for i in range (5):
    idade=int(input(f"escreva a idade do {i+1}° aluno: "))
    altura=float(input(f"escreva a altura do {i+1}° aluno: "))
    idades.append(idade)
    alturas.append(altura)

media=sum(alturas)/30

cont=0

for i in range (5):
    if idades[i] > 13 and alturas[i] < media:
        cont+=1

print("a quantidade de alunos com idade superior a 13 e altura inferior a media de altura da turma é: ",cont)


