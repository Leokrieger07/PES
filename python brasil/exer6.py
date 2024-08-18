medias=[0]*10
cont=0

for i in range (10):
    notas=[0] 
    print(f"Escreva as notas do {i+1}° aluno")
    for j in range (4):
        nota=float(input(f"escreva a sua {j+1}° nota: "))
        notas.append(nota)
    
    media= sum(notas) / 4
    medias.append(media)

    if media >=7:
        cont+=1

print("o numero de alunos aprovados com nota maior ou igual a 7 foi: ",cont)