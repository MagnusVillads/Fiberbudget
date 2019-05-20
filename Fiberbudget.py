import math

def main():
    print()

def konnektering():
    global sumkonnektering
    print()
    talkonnektering = int(input("Tast Hvor Mange Konnekteringer Du Har "))
    sumkonnektering = (talkonnektering * 0.5)
    print()


def splidsning():
    global sumsplidsning
    print()
    talsplids = int(input("Tast Hvor Mange Splidsninger Du Har "))
    sumsplidsning = (talsplids * 0.1)
    print()


def fiberlængde():
    global talfiberlængde
    print("Fiber længde")
    print()
    talfiberlængde = float(input("Tast Antal Km "))
    print()

def sikk():
    global sumsikk
    sumsikk = 3

def rep():
    global sumrep
    sumrep = (math.ceil(talfiberlængde/10)*0.5)




def db1310sm():
    global sumdb1310sm
    sumdb1310sm = (talfiberlængde * 0.35)


def db1550():
    global sumdb1550
    sumdb1550 = (talfiberlængde * 0.20)

def db850():
    global sumdb850
    sumdb850 = (talfiberlængde * 2.5)

def db1310mm():
    global sumdb1310mm
    sumdb1310mm = (talfiberlængde * 0.6)

main()

wh=1

while wh==1:
    fiberlængde()

    splidsning()

    konnektering()

    rep()

    sikk()

    db850()

    db1310mm()

    db1310sm()

    db1550()

    if talfiberlængde <= 1:
        print("Du Skal Bruge En MultiModeFiber På 850nm")
        print("Dit Tab =", talfiberlængde + sumsplidsning + sumkonnektering + sumsikk + sumrep + sumdb850 ,"db")
        print()
        start=int(input("Tast 1 For At Starte Igen. Tast 2 For At Stoppe "))
        if start ==1:
            main()
        else:
            break


    elif talfiberlængde <= 2:
        print("Du Skal Bruge En MultiModeFiber På 1310nm")
        print("Dit Tab =", talfiberlængde + sumsplidsning + sumkonnektering + sumsikk + sumrep + sumdb1310mm ,"db")
        print()
        start=int(input("Tast 1 For At Starte Igen. Tast 2 For At Stoppe "))
        if start ==1:
            main()
        else:
            break


    elif talfiberlængde <= 10:
        print("Du Skal Bruge En SingleModeFiber På 1310nm")
        print("Dit Tab =", talfiberlængde + sumsplidsning + sumkonnektering + sumsikk + sumrep + sumdb1310sm ,"db")
        print()
        start=int(input("Tast 1 For At Starte Igen. Tast 2 For At Stoppe "))
        if start ==1:
            main()
        else:
            break


    elif talfiberlængde > 10:
        print("Du Skal Bruge En SingleModeFiber På 1550nm")
        print("Dit Tab =", talfiberlængde + sumsplidsning + sumkonnektering + sumsikk + sumrep + sumdb1550 ,"db")
        print()
        start=int(input("Tast 1 For At Starte Igen. Tast 2 For At Stoppe "))
        if start ==1:
            main()
        else:
            break

print()
print("Programmet Stopper Nu!")
