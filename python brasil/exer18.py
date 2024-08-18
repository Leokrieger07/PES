notas=[]
media=0

quant=int(input("escreva a quantidade de alunos da turma: "))

for i in range(quant):
    n=float(input(f"Escreva a nota do {i+1}° aluno: "))
    notas.append(n)
    media+=n

print("\nESTATÍSTICAS:")

media=media/quant

print("\nmedia das notas da turma: ",round(media, 2))

maior=n
for n in notas: 
    if n>maior:
        maior=n

print("maior nota da turma: ",maior)

menor=n
for n in notas:
    if n<menor:
        menor=n

print("menor nota da turma: ",menor)

cont=0

for n in notas:
    if n>media:
        cont+=1

print("quantidade de notas acima da media: ",cont)