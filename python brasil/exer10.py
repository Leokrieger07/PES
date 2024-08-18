a=[]*10
b=[]*10
c=[]*20

for i in range (10):
    n=int(input(f"escreva o {i+1}° numero para o vetor A: "))
    a.append(n)

for i in range (10):
    n=int(input(f"escreva o {i+1}° numeropara o vetor B: "))
    b.append(n)


for i in range (10):
    c.append(a[i])
    c.append(b[i])

print("o vetor A é: ",a)
print("o vator B é: ",b)
print("o vetor intercalado dos 2 outros vetro é: ",c)

