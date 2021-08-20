'''
Pentru compresia unui şir binar se foloseşte tehnica White Block Skipping
adaptat - ignorarea blocurilor (grupelor)uniforme (compuse numai din biţi
de 0 sau numai din biţi de 1). Şirul este împărţit în blocuri (grupe) de
câte n biţi, codate independent. Există două codări posibile: codarea în
care se ignoră blocurile compuse numai din biţi 0, şi codarea în care se
ignoră blocurile compuse numai din biţi 1. In final, se alege codarea care
asigură raportul maxim de compresie.In cazul în care cele două variante de
compresie ajung la acelaşi raport de compresie, se utilizează varianta în
care se ignoră blocurile compuse numai din biţi 0.
Pentru codarea în care se ignoră blocurile compuse numai din biţi 0, şirul
comprimat începe cu un bit 0, la care se adaugăcodurile corespunzătoare
blocurilor de biţi din şirul iniţial, codate după regula următoare: dacă
toţi biţii blocului sunt nuli, blocul este înlocuit de un bit unic de zero;
dacă cel puţin un bit din bloc este nenul, atunci biţii blocului se copiază
şi în faţa lor este adăugat un bit de 1 (ca prefix). 
Pentru codarea în care se ignoră blocurile compuse numai din biţi 1, şirul
comprimat începe cu un bit 1, la care se adaugă codurile corespunzătoare
blocurilor de biţi din şirul iniţial, codate după regula următoare: dacă
toţi biţii sunt 1, blocul este înlocuit de un bit unic de 1; dacă cel puţin
un bit din bloc este nul, atunci biţii blocului se copiazăşi în faţa lor
este adăugat un bit de 0 (ca prefix).

Cerință
Dându-se un număr N pozitiv reprezentand numărul de elemente din şir, apoi
numărul n pozitiv reprezentând numărul de elemente din fiecare bloc ce va fi
codat, apoi cele N elemente ale şirului, să se genereze şirul comprimat
(codat) şi săse calculeze raportul de compresie (raportul dintre numărul de
biţi din şirul iniţial - N - şi numărul de biţi din şirul comprimat). Dacă
şirul de intrare nu poate fi împărţit exact în grupe de n biţi, ultimii biţi
rămaşi se codează ca şi când ar face parte dintr-un grup neuniform (dar fără
a adăuga biţi de completare).

Date de intrare
Pe prima linie se află numărul întreg pozitiv N, reprezentând numărul de
elemente din şir, urmat de caracterul newline, apoi numărul întreg pozitiv
n, reprezentând numărul de elemente din fiecare grupă, urmat de caracterul
newline. Pe următoarele N linii se află elementele şirului (numere de 0 sau 1),
câte unul pe linie, urmat de caracterul newline.

Date de ieșire
Se va afișa pe prima linia valoarea raportului de compresie, cu două zecimale,
cu rotunjire, apoi şirul comprimat, câte un număr (0 sau 1) pe fiecare linie. 

Restricții și precizări
1. 8<N<= 1024
2. 2 < n <= 8
3. Orice element al şirului este un număr întreg pozitiv pe 8 de biți.
'''

N = int(input())

if N >= 8 and N <= 1024:
    n = int(input())
    if n >= 2 and n <= 8:
        elem = [""]*N
        rc0 = 0   # rata compresie
        rc1 = 0
        sc0 = "0" # sir codat
        sc1 = "1"
        for i in range(N):
            elem[i] = int(input())
            if elem[i] != 0 and elem[i] != 1:
                print("element incorect!")
                break
        i = 0
        while i < N:
            nul = 0
            nenul = 0
            grupa = ""
            j = 0
            while j < n :
                if i+j < N:
                    if elem[i+j] == 0:
                        nul += 1
                        grupa += str(elem[i+j])
                    elif elem[i+j] == 1:
                        nenul += 1
                        grupa += str(elem[i+j])
                    j += 1
                elif i+j >= N:
                    j += 1   
                    

            if nul == n and nenul == 0:
                sc0 += "0"
                sc1 += "0" + grupa
            elif nul == 0 and nenul == n:
                sc0 += "1" + grupa
                sc1 += "1"
            elif (nul != 0 and nenul != 0) or nul + nenul < n:
                sc0 += "1" + grupa
                sc1 += "0" + grupa
            i += n
        rc0 = N/len(sc0)
        rc1 = N/len(sc1)
        print("\n")
        if rc1 > rc0:
            print("{0:.2f}".format(rc1))
            for x in sc1:
                print(x)
        else:
            print("{0:.2f}".format(rc0))
            for x in sc0:
                print(x)
            
    else:
        print("Numar de elemente din grupa incorect!")
else:
    print("Numar de valori incorect!")



