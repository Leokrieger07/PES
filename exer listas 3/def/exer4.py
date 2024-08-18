def soma_lista(lista):
    return sum(lista)


numeros=[]

for i in range(4):
    n=float(input(f"Escreva o {i+1}° numero: "))
    numeros.append(n)

result=soma_lista(numeros)

print("a soma dos numeros digitados é igual a: ",result)

