numero1=int(input("Introduce un número:"))
numero2= int(input("Introduce otro número:"))
numero3= int(input("Introduce otro número:"))

if numero1<numero2<numero3:
        print("Están en orden ascendente")
elif (numero1==numero2==numero3):
    print("Se repiten todos los números")
elif (numero1==numero2):
        print("Se repiten el primer y segundo número, prueba otra vez")
elif (numero2==numero3):
     print("Se repiten el segundo y tercer número, prueba otra vez")
elif (numero1 == numero3):
     print("Se repiten el primer y tercer número, prueba otra vez")
elif (numero1 == 0) or (numero2==0) or (numero3==0):
    print("Hay un 0, prueba otra vez")
else:
    print("No están en orden ascendente")

####
print("\n\n\n")

lista_numeros=[]
print("Introduce 3 números")
for x in range(3):
    lista_numeros.append(input("Introduce un número:"))
print(lista_numeros)

if lista_numeros[0]<lista_numeros[1]<lista_numeros[2]:
        print("Están en orden ascendente")
elif (lista_numeros[0]==lista_numeros[1]==lista_numeros[2]):
    print("Se repiten todos los números")
elif (lista_numeros[0]==lista_numeros[1]):
        print("Se repiten el primer y segundo número, prueba otra vez")
elif (lista_numeros[1]==lista_numeros[2]):
     print("Se repiten el segundo y tercer número, prueba otra vez")
elif (lista_numeros[0] == lista_numeros[2]):
     print("Se repiten el primer y tercer número, prueba otra vez")
elif (lista_numeros[0] == 0) or (lista_numeros[1]==0) or (lista_numeros[2]==0):
    print("Hay un 0, prueba otra vez")
else:
    print("No están en orden ascendente")
        
####
print("\n\n\n")
secuencia_letras=input("Introduce una secuencia de letras:")
a_en_texto=secuencia_letras.count('a')
enunciado= print("Escribe una secuencia de letras o un punto para terminar")
def cadena_a (enunciado):  
    while True:
        secuencia_letras=input("Introduce una secuencia de letras:")
        a_en_texto=secuencia_letras.count('a')
        print("En esta secuencia hay", a_en_texto, "'a'")
        if "." in secuencia_letras:
         break
    return "En esta secuencia hay", a_en_texto, "a"
print(cadena_a(enunciado))