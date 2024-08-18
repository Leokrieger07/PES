a=[]*10
soma=0

for i in range (5):
    n=int(input(f"Escreva o {i+1}° numero: "))
    a.append(n)

for n in a :
    soma=soma + n^2

print(soma)