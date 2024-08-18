def c_media(v1,v2,v3):
    media = (v1+v2+v3)/3
    return media

v1=float(input("escreva a sua nota 1:"))
v2=float(input("escreva a sua nota 2:"))
v3=float(input("escreva a sua nota 3:"))

media = c_media(v1,v2,v3)

print(media)