def area (p,r,h):
    return 2 * p * r * (r + h)

p=3.14

r=float(input("escreva o raio do cilindro: "))
h=float(input("escreva a altura do cilindro: "))

result = area(p,r,h)

print(f"a area do cilindro é:, {result:.2f}")