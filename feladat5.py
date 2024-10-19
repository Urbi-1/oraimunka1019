import math
def ot():
    szam = int(input("Kérem adjon meg egy 40 és 95 közötti számot!"))
    if szam <40 or  szam > 95:
        print("HIBA: nem megfelelő szám!")
    else:
        #megoldás1
        szam = str(szam)
        print(szam[0])

        #megoldás2
        szam = int(szam)
        print(str(int(szam/10)))

        #megoldás3
        szam = int(szam)
        print(str(math.floor(szam/10)))