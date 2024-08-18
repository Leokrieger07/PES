notasaluno=[]
cont=0
media=0
soma=0
print("escreva as suas 4 notas")

for i in range(4):
    nota=int(input(f"escreva a sua nota de número {i+1} "))
    notasaluno.append(nota)
    cont+=1
    soma+=nota

media=soma/cont

if media>=6:
    print("você foi aprovado com media", media)
else:
    print("você foi reprovado com media", media)




