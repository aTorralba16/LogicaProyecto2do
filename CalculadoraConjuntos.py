import random
import os 
import string 

def con():
    n = int(input("Cantidad de elementos en el Conjunto: "))
    ll = []
    for i in range(n):
        s = input(f"Elemento {i + 1}: ")
        ll.append(s)
    return ll

def alea(n):
    ll = []
    for _ in range(n):
        tipo = random.choice(['num', 'let', 'cad'])
        
        if tipo == "num":
            ll.append(random.randint(0, 100))  
        elif tipo == "let":
            ll.append(random.choice(string.ascii_letters)) 
        elif tipo == "cad":
            long = random.randint(2, 5)  
            cadena = "".join(random.choices(string.ascii_letters + string.digits, k=long))
            ll.append(cadena)
    return ll

def union(A,B):
    uni = A
    ab = len(B)
    for i in range(ab):
        if B[i] not in uni:
            uni.append(B[i])
    return uni

def ints(A,B):
    l = []
    for i in A:         
        if i in B and i not in l:
            l.append(i)
    return l

def dif(A, B):
    rest = []
    for i in A:
        if i not in B:
            rest.append(i)    
    return rest

def sim(A, B):
    siml = []
    for i in A:
        if i not in B:
            siml.append(i)
    for d in B:
        if d not in A:
            siml.append(d)
    return siml

def univ(A, B, C):
    uni = []
    for lista in [A, B, C]:
        for i in lista:
            if i not in uni:
                uni.append(i)
    return uni

def com (A, uni):
    comp = []
    for i in uni:
        if i not in A:
            comp.append(i)    
    return comp

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def ver(ls):
    while len(ls) != 3:
        print("Seleccion incorrecta ingresela de nuevo")
        sl = input("Ingrese la operacion: ")
        ls = sl.split()

doc = {
    "U": union,
    "^": ints,
    "-": dif,
    "∆": sim,
    "C": com,
    "⊂": Subconjuntos,
    "⊃": SubconjuntoPropio,
    "==": igual,
    "!=": NoIguales,

}

#Programa principa;
print("Calculadora de conjuntos")
sel = input(("Hacer conjuntos aleatorios? (Y/N): ")).upper().strip()
while sel != "Y" and sel != "N":
    print("Entrada incorrecta")
    sel = input(("Hacerlo aleatorio? (Y/N): ")).upper().strip()

if sel == "N":
    print("Entrada del primer conjunto")
    a1 = con()
    print("Ingrese el segundo conjunto")
    b1 = con()
    print("Ingrese el tercer conjunto")
    c1 = con()

else:
    n = int(input("Cantidad de elementos por conjunto: "))
    a1 = alea(n)
    b1 = alea(n)
    c1 = alea(n)

limpiar()
uni = univ(a1,b1,c1)
print(f"A:{a1}")
print(f"B:{b1}")
print(f"C:{c1}")
print(f"Universo:{uni}")
print("Operaciones: U (union), ^ (interseccion), - (diferencia), ∆ (dif. sim.) y C (complemento), -1 para terminar.")

tmdc = {"A": a1, "B": b1, "C": c1}

sl = ""
while sl != "-1": 
    sl = input("Ingrese la operacion: ")
    
    if sl == "-1":
        break

    ls = sl.split()
    ver(ls)
    c1 = ls[0]
    op = ls[1]
    c2 = ls[2]

    c11 = tmdc.get(c1)
    c22 = tmdc.get(c2)
    if op == "C":
        c22 = uni

    res = doc[op](c11,c22)
    print(res)
# *** SUBCONJUNTOS ***
def Subconjuntos (A,B):
    for i in A:
        if i not in B:
            return False # Si un elemento no es igual no es un subconjunto
    return True

def igual(A,B):
    if Subconjuntos(A, B) and Subconjuntos(B,A):
        return True # Son iguales
    return False # No son iguales

def SubconjuntoPropio(A,B):
    if Subconjuntos(A,B) and not igual(A,B):
        return True
    return False

def NoIguales(A,B):
    for i in A:
        if i in B:
            return False #Si un elemento es igual rompe   ⅭↃ⋃⋂⊑⊒
    return True