a=[]*10
b=[]*10
c=[]*10
d=[]*30

for i in range (10):
    n=int(input(f"escreva o {i+1}° numero para o vetor A: "))
    a.append(n)

for i in range (10):
    n=int(input(f"escreva o {i+1}° numero para o vetor B: "))
    b.append(n)

for i in range (10):
    n=int(input(f"escreva o {i+1}° numeroo para o vetor C: "))
    c.append(n)

for i in range (10):
    d.append(a[i])
    d.append(b[i])
    d.append(c[i])

print("o vetor a é: ",a)
print("o vetor b é: ",b)
print("o vetor c é: ",c)
print("\n o vetor intercalado dos outros 3 vetores é: ",d)