'''
Doamna secretară trebuie să stabilească numărul de studenți ce vor lua bursă
de merit în anul universitar următor și să identifice studentul care va lua
bursa de performanță (există o singură bursă de performanță).
Are la dispozițielista tuturor studenților și notele obținute de aceștia la
diversele discipline. Bursa de performanță se acordă studentului integralist
cu media cea mai mare. Bursele de merit se acordă în ordinea descrescătoare
a mediilor, în limita numărului maxim de burse, tuturor studenților integraliști
care au media generală peste 8.00.

Cerinţă
Stabiliți ce student va lua bursă de performanță și câți studenți vor lua bursă
de merit în anul universitar următor.

Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date:
• Trei numere întregi pozitive m, n, p separate prin spaţiu, reprezentând
o m – numărul de studenţi,
o n – numărul de discipline,
o p – numărul de burse de merit disponibile;
• 2*m linii de pe care se citesc, în ordine, în formatul:
o <NS>, un şir de caractere reprezentând numele studentului;
o <N1> <N2> ... <Nn>, n numere întregi din intervalul 1 – 10 separate prin spaţiu 
reprezentând notele obţinute de respectivul student la cele m discipline;
Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline
(tasta Enter).

Date de ieşire
Programul va afișa pe ecran (stream-ul standard de ieșire):
• Pe prima linie: numărul de studenți ce vor lua bursă de merit
• Pe a doua linie: numele studentului care va lua bursă de performanță și media
lui (număr fracționar cu 2 zecimale) separate prin spațiu.

Restricţii şi precizări
1. 0 < m, n, p < 100
'''
m, n, p = input().split()
m = int(m)
n = int(n)
p = int(p)
if m > 0 and m < 100 and n > 0 and n < 100 and p > 0 and p < 100:
    NS = []
    N = []
    integr = {} 

    for i in range(m):
        NS = str(input())
        N = list(map(int,input().strip().split()))[:n]
        ok = 1
        integralist = 1
        suma = 0

        for j in range(len(N)):
            suma += N[j]
            if N[j] < 1 or N[j] > 10:
                ok = 0
            if N[j] < 5:
                integralist = 0
        if ok == 0:
            print("Note incorecte!")
            break
        elif integralist == 1:
            media = round(suma/n, 2)
            integr[NS] = media 
    sort_integr = sorted(integr.items(), key=lambda x: x[1], reverse = True)
    bursa_perf = sort_integr[0][0] + " " + "{:.2f}".format(sort_integr[0][1])

    for i in range(len(sort_integr)):
        if i == 0:
            bursa_merit = 0
        elif float(sort_integr[i][1]) >= 8.00 and p > 0:
            bursa_merit += 1
            p -= 1
            
    print(bursa_merit)    
    print(bursa_perf)        
else:
    print("Numerele introduse trebuie sa apartina intervalului (0, 100).")























