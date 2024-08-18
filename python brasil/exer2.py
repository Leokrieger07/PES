numeros=[""]

for i in range(10):
    n=float(input(f"escreva o seu valor numero {i+1}: "))
    numeros.append(n)

print("Números na ordem inversa: ")

for n in reversed(numeros):
    print(n)