notas=[]
cont=0
n=0
contm=0
abaixo=0

while True:
    n=float(input("escreva a sua nota: "))
    if n==-1:
        break
    cont+=1
    notas.append(n)

print("\na quantidade de valores lidos foi: ",cont)

print("\nvalores informados, um ao lado do outro: ",notas)

print("\n valores informados um abaixo do outro na ordem inversa em que foram lidos: ")
for n in reversed (notas):
    print(n)

print("\na soma dos valores digitados é: ",sum(notas))

media= sum(notas) / len(notas)

print("\na media dos valores digitados é: ",media)

for n in notas:
    if n>media:
        contm+=1
print("\na quantidade de valores acima da media calculada é: ",contm)

for n in notas:
    if n < 7:
        abaixo+=1

print("\na quantidade de valores abaixo de 7 é: ",abaixo)

print("obrigado por usar o programa !")
