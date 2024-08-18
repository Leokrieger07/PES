temperaturas=[]
mes=['janeiro', 'fevereiro','março','abril', 'maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

for i in range (12):
    temp=float(input(F"Escreva a temperatura média do {i+1}° mes: "))
    temperaturas.append(temp)

media=sum(temperaturas)/len(temperaturas)

print("\nmeses em que a temperatura foi maior doo que a media de temperatura do ano: ")
for i in range (len(temperaturas)):
    if temperaturas[i] > media:
        print("\nno mes de", mes[i], "tivemos uma media de temperatura de", temperaturas[i],"°C")

print("a media de temperatura do ano foi: ",media)



