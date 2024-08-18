quant=int(input("escreva a quantidade de notas: "))
soma=0
media=0

for i in range(quant):
    x=int(input(f"escreva sua nota de numero {i+1}: "))
    soma+=x

media=soma/quant
if media>=6:
    print("você foi aporvado com média: ",media) 
else:
    print(" você foi reprovado com media: ",media)