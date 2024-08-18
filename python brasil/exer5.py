numeros=[""]*20
impar=[""]*20
par=[""]*20

for i in range (20):
    n=int(input(f"escreva o eu {i+1}° numero: "))
    numeros.append(n)
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)

print("numeros digitados: ")
for n in numeros:
    if n!="":
        print(n)

print("numeros pares digitados: ")
for n in par:
    if n!="":
        print(n)

print("numeros impares digitados: ")
for n in impar:
    if n != "":
        print(n)