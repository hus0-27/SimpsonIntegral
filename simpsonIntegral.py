import math
import time


pi = math.pi

def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)
def e(x):
    return math.exp(x)

func = input("la Fonction: ")
print()
a = eval(input("premier borne d'integral: "))
print()
b = eval(input("dernier borne d'integral: "))
print()
n = int(input("nombre de divisions: "))
print()
h = (b - a)/n

def F(x):
    F = eval(func)
    return F

limites = F(a) + F(b)
impaires , paires = 0 , 0
print()
print()
print("h: " , h ,", fonctions on limite: " ,  limites)
print()
print()
print("impaires: ")
print()
print()
i = 1
while i < n :
    impaires = impaires + 4 * F(a+(i*h))
    print(i ," , ", impaires)
    i+=2
print()
print("paires: ")
print()
print()
j = 2
while j < n-1 :
    paires = paires + 2 * F(a+(j*h))
    print(j ," , ", paires)
    j+=2
print()
print()
print()
print("Solution:" , h/3.0 * (limites + impaires + paires))
print()
print()
time.sleep(1.5)

input("appuyez sur entrée pour sortir...")