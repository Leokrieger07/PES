idades=[]*5
alturas=[]*5

for i in range (5):
    idade=int(input("escreva a sua idade: "))
    idades.append(idade)

for i in range (5):
    altura=float(input("\nescreva a sua altura: "))
    alturas.append(altura)

for idade in reversed(idades):
    print(idade)

for altura in reversed(alturas):
    print(altura)

