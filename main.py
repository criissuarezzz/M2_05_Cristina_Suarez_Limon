from timeit import repeat
from turtle import end_fill


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
Enunciado = input("Introduce una secuencia de letras: ")
contador_a = 0
for letra in Enunciado:
  if letra == "a":
    contador_a = contador_a + 1
  elif Enunciado == ".":
    break
print("En la secuencia de letras hay", contador_a,  "letras a.")


#######
print("\n\n\n")
lista_palabras=['Parada', 'Moto', 'panda','pato', 'tapa', 'socorrista', 'edificio', 'Wi-Fi']
print(lista_palabras[0], len(lista_palabras[0]))
print(lista_palabras[1], len(lista_palabras[1]))
print(lista_palabras[2], len(lista_palabras[2]))
print(lista_palabras[3], len(lista_palabras[3]))
print(lista_palabras[4], len(lista_palabras[4]))
print(lista_palabras[5], len(lista_palabras[5]))
print(lista_palabras[6], len(lista_palabras[6]))    
print(lista_palabras[7], len(lista_palabras[7]))


def mas_grande(lista_palabras):
    max=len(lista_palabras[0])
    for x in lista_palabras:
        if x>max:
            max=0
    return max
print("La palabra más larga es", mas_grande(len(lista_palabras)))