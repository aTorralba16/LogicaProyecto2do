import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Emisores y receptores
A = []
B = []
ll = []
con = []

def menu():
    print("1.- Agregar Emisor")
    print("2.- Agregar Receptor")
    print("3.- Eliminar Emisor")
    print("4.- Eliminar Receptor")
    print("5.- Agregar llave")
    print("6.- Eliminar llave")
    print("7.- Crear coneccion")
    print("8.- Ver propiedades de funcion")
    print("9.- Ver propiedades de relacion")
    print("10.- Calculadora")
    print("0.- Salir")

def valor():
    valor = input("Ingrese valor: ")
    if valor.isdigit():
        return int(valor)
    return valor

def funcion():
    us = []
    for e, k, r in con:
        if e in us:
            return False
        us.append(e)
    return True

def inyectiva():
    us = []
    for e, k, r in con:
        if r in us:
            return False
        us.append(r)
    return True

def sobreyectiva():
    us = []
    for e, k, r in con:
        if r not in us:
            us.append(r)
    for r in B:
        if r not in us:
            return False
    return True

def biyectiva():
    return inyectiva() and sobreyectiva()

def reflexiva():
    for x in A:
        if (x, x) not in [(e, r) for (e, k, r) in con]:
            return False
    return True

def simetrica():
    par = [(e, r) for (e, k, r) in con]
    for a, b in par:
        if (b, a) not in par:
            return False
    return True

def transitiva():
    par = [(e, r) for (e, k, r) in con]
    for a, b in par:
        for x, c in par:
            if b == x and (a, c) not in par:
                return False
    return True

def calculadora(A,B,ll):
    import os 

    def union(A,B):
        uni = A[:]
        for i in B:
            if i not in uni:
                uni.append(i)
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
        return ls

    def Subconjuntos (A,B):
        for i in A:
            if i not in B:
                return False
        return True

    def igual(A,B):
        return Subconjuntos(A, B) and Subconjuntos(B,A)

    def SubconjuntoPropio(A,B):
        return Subconjuntos(A,B) and not igual(A,B)

    def disjuntos(A, B):
        for elemento in A:
            if elemento in B:
                return False
        return True

    doc = {
        "U": union,
        "^": ints,
        "-": dif,
        "∆": sim,
        "C": com,
        "⊂": Subconjuntos,
        "⊃": SubconjuntoPropio,
        "==": igual,
        "dis": disjuntos,
    }

    print("Calculadora de conjuntos")

    a1 = A
    b1 = B
    c1 = ll

    limpiar()
    uni = univ(a1,b1,c1)

    print(f"A:{a1}")
    print(f"B:{b1}")
    print(f"C:{c1}")
    print(f"Universo:{uni}")

    print("Operaciones: U (union), ^ (interseccion), - (diferencia), ∆ (dif. simetrica) \n, " \
    "C (complemento), ⊂ (subconjunto), ⊃ (subc. propio), == (igaules), dis (disjuntos), -1 para salir")

    tmdc = {"A": a1, "B": b1, "C": c1}

    sl = ""
    while sl != "-1": 
        sl = input("Ingrese la operacion: ")
        
        if sl == "-1":
            break

        ls = sl.split()
        ls = ver(ls)  

        c_1 = ls[0]  
        op = ls[1]
        c_2 = ls[2]  

        if op not in doc:  
            print("Operacion no valida")
            continue

        c11 = tmdc.get(c_1)
        c22 = tmdc.get(c_2)

        if c11 is None or c22 is None:  
            print("Conjunto no valido")
            continue

        if op == "C":
            c22 = uni

        res = doc[op](c11,c22)
        print(res)

while True:
    menu()
    sel = input("Seleccione funcion: ")

    match sel:
        case "1":
            limpiar()
            print("Agregar emisor")
            ag = valor()
            while ag in A:
                print("Emisor ya existente")
                ag = valor()
            A.append(ag)
            limpiar()
            print(f"Emisores actuales: {A}")

        case "2":  
            limpiar()
            print("Agregar receptor")
            rec = valor()
            while rec in B:
                print("Receptor ya existente")
                rec = valor()
            B.append(rec)
            limpiar()
            print(f"Receptores actuales: {B}")

        case "3":  
            limpiar()
            print("Eliminar emisor")
            emi = valor()
            while emi not in A:
                print("Emisor no existente")
                emi = valor()
            A.remove(emi)
            limpiar()
            print(f"Emisores actuales: {A}")

        case "4": 
            limpiar()
            print("Eliminar receptor")
            re = valor()
            while re not in B:
                print("Receptor no existente")
                re = valor()
            B.remove(re)
            limpiar()
            print(f"Receptores actuales: {B}")

        case "5":
            limpiar()
            print("Agregar llave")
            ag = valor()
            while ag in ll:
                print("Llave ya existente")
                ag = valor()
            ll.append(ag)
            limpiar()
            print(f"Llaves actuales: {ll}")

        case "6":
            limpiar()
            print("Eliminar llave")
            re = valor()
            while re not in ll:
                print("Llave no existente")
                re = valor()
            ll.remove(re)
            limpiar()
            print(f"Llaves actuales: {ll}")

        case "7":
            limpiar()
            print("Crear conexión (Emisor, Llave, Receptor)")
            e = valor()
            while e not in A:
                print("Emisor no existe")
                e = valor()
            k = valor()
            while k not in ll:
                print("Llave no existe")
                k = valor()
            r = valor()
            while r not in B:
                print("Receptor no existe")
                r = valor()
            nueva = (e, k, r)
            if nueva in con:
                print("Conexion ya existente")
            else:
                con.append(nueva)
                print("Conexion agregada:", nueva)
                print("Conexiones actuales:", con)

        case "8":
            limpiar()
            print("Propiedades de función")
            print("Es función:", "SI" if funcion() else "NO")
            print("Inyectiva:", "SI" if inyectiva() else "NO")
            print("Sobreyectiva:", "SI" if sobreyectiva() else "NO")
            print("Biyectiva:", "SI" if biyectiva() else "NO")
            input("\nPresiona Enter para continuar...")
            limpiar()

        case "9":
            limpiar()
            print("Propiedades de relacion")
            print("Reflexiva:", "SI" if reflexiva() else "NO")
            print("Simetrica:", "SI" if simetrica() else "NO")
            print("Transitiva:", "SI" if transitiva() else "NO")
            input("\nPresiona Enter para continuar...")
            limpiar()

        case "10":
            calculadora(A, B, ll)

        case "0":
            print("Saliendo...")
            break

        case _:  
            limpiar()
            print("Entrada no valida.")