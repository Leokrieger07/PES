x = int(input("Digite um número: "))

if x > 0:
    i = 1
    while i <= x:
        print(i)
        i = i+1
elif x < 0:
    i = -1
    while i >= x:
        print(i)
        i = i-1
else:
    print("Número é zero.")

