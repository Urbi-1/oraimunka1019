import math
def negyes():

    n=1
    k=1
    if (k % 2 == 1) and (n >0) and (pow(2,n)>k):
        proth = (k* math.pow(2,n)) + 1
        print("Proth-számok: ", end="")
        for n in range(0, 10, 1):
            proth= (k * math.pow(2, n)) + 1
            print(str(proth)+ ", ", end="")
        proth = (k * math.pow(2, 10)) + 1
        print(proth)
    else:
        print("HIBA: Nem megfelelő számok!")
pass

def negyesb():
    n = 1
    k = 1
    szamlalo = 0
    print("Proth-számok: ", end="")
    while szamlalo < 10:
        if (k % 2 == 1) and (n > 0) and (pow(2, n) > k):
            if szamlalo != 9 :
            szamlalo += 1
            proth = (k * math.pow(2, n)) + 1
            print(str(proth) + ", ", end="")
        else:
            print("HIBA: Nem megfelelő számok!")
            proth = (k * math.pow(2, 10)) + 1
            print(proth)
        n += 1
    pass

def negyesc():
    n = 1
    k = 1
    print("Proth-számok: ", end="")
    while n < 10:
        if (k > 0) and (k% 2 == 1) and (n > 0) and (2**n > k):
            szam = k*2**n+1
            print(str())

    pass