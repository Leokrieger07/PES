notas=[]

for i in range (4):
    n=float(input(f"Escreva a sua {i+1}° nota: "))
    notas.append(n)

m=sum(notas)/len(notas)

if m>=6 :
    print("você foi aprovado(a)!")
else:
    print("você foi reprovado(a).")