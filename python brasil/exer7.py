numeros=[]*5
soma=0
m=1

for i in range (5):
    n=int(input(f"escreva o {i+1}° numero: "))
    numeros.append(n)

soma = sum(numeros)

for n in numeros:
    m = m*n

print("\na soma dos numeros digitados é: ",soma)
print("\na multiplicação dos numeros digitados é: ",m)