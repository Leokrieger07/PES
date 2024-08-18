idadealuno=[]
print("informe a idade dos 6 alunos")

for i in range (6):
    idade=int(input(f"digite a idade do aluno número {i+1} "))
    idadealuno.append(idade)
    
print("idade dos alunos com idade igual ou maior a 16 anos:")
for idade in idadealuno:
    if idade>=16:
        print(idade)