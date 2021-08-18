'''
Un studiu de marketing cerut de o galerie de artă mai excentrică a arătat că,
în mod surprinzător, clienţii analizează o perioadă mai mare de timp
exponatele care au preţuri ce pot fi exprimate ca un palindrom şi de obicei
le preferă, chiar şi în cazul în care un alt obiect similar are un preţ cevamai 
scăzut. Pe de altă parte, din anumite motive (doar de ei ştiute) artiştii,
care creează aceste produse,vor ca numerele care definesc preţul unui obiect
de artă sa fie atent elaborate şi să conţină doar anumite cifre considerate
de ei ca fiind foarte importante. Sub aceste constrângeri, proprietarii 
galeriei de artă vor să maximizeze câştigurile şi să afişeze cele mai mari
preţuri posibile în condiţiile menţionate.
Astfel, se cere să se realizeze un program care interpretează o secvenţă de
cifre nenule oferite la intrare, în vederea obţinerii unor reprezentări
zecimale (numere în bază 10). Plecând de la cifrele oferite sunt posibile
mai multe reprezentări zecimale. Dintre numerele zecimale astfel obţinute
se va alege cel mai mare număr care are proprietatea de palindrom (vedeţi
explicaţiile de mai jos).

Date de intrare 
La intrarea programului, pe prima linie se prezintă un număr natural n,
iar pe a doua linie n cifre, separate prin câte un spaţiu. Cu aceste
cifre se pot construi numere în baza 10.Fiecare dintre cele două linii
de intrare se încheie cu caracterul newline (\n), obţinut prin apăsarea 
tastei Enter.

Date de ieşire 
Să se determine numărul cel mai mare de tip palindrom (în situaţia în
care se pot forma mai multe palindromuri) ce se poate forma cu toate
cifrele conţinute pe a doua linie. Programul va afişa la consolă (pe
stream-ul stdout) numărul astfel determinat urmat de caracterul newline
(\n) (tastaEnter).
Dacă nu se poate forma niciun palindrom, la ieşire se va afişa cifra 0 (zero);
dacă se poate forma un singur palindrom, acesta, evident, se va afişa la ieşire
ca atare.

Restricţii şi precizări
1. Numărul n este un număr natural, în gama 2 < n < 20.
2. Cifrele citite pe cea de-a doua linie sunt în gama [1; 9].
3. Prin număr palindromic se înţelege acel număr care are formă identică,
fie că este citit de la stânga la dreapta, fie de la dreapta la stânga.
Conform restricţiei 1, acesta va avea cel puţin trei cifre. Exemple: 313,
2992, 52725, 193391 etc
'''
n = int(input())

if n > 2 and n < 20 :
    x = [0,0,0,0,0,0,0,0,0,0]
    cifre = input().split()
    i = 0
    while i < n:
        if int(cifre[i]) < 1 or int(cifre[i]) > 9 :
            print("Cifre introduse incorect!")
        else:
            x[int(cifre[i])] += 1
            cifre[i] = int(cifre[i])
        i += 1

    impare = 0
    i = 0
    result = 0
    nr = 0
    while i < len(x):
        if x[i] != 0 and x[i] % 2 != 0:
            impare += 1
            nr = i
        i += 1

    if impare > 1:
        result = 0
    elif impare == 1 or impare == 0:
            dec = 1
            i = 0
            while i < x[nr]:
                result += nr*dec
                dec *= 10
                i += 1
            x[nr] = 0
            i = 0
            while i < len(x):
                if x[i] != 0:
                    j = 0
                    while j < x[i]:
                        result += i*dec
                        result *= 10
                        result += i
                        dec *= 100
                        j += 2
                    x[i] = 0
                i += 1
            
    print(result)
        
else:
    print("Numarul de cifre trebuie sa apartina intervalului (2, 20).")

