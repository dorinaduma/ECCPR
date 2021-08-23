'''
Pentru a deveni competitivă în domeniul Blockchain și a monedelor virtuale,
firma la care lucrați a dezvoltat un algoritm de hashing inovativ pentru
valori numerice. Algoritmul funcționează în modul următor: asupra unui număr
natural se face următoarea transformare: dacă numărul are cel puțin două 
cifre, se iau pe rând din număr câte două cifre vecine și se scade cea mai
mică din cea mai mare. Cu cifrele astfel obținute se formează un nou număr.
De exemplu, pentru numărul 5734, din cifrele 5 și7 se obține 2, din 7 și 3
se obține 4 iar din 3 și 4 se obține 1. Formăm deci un nou număr 241, căruia 
i se poate aplica aceeași transformare, obținându-se 23. Din 23, prin același
procedeu, obținem 1.
Dacă numărul este format dintr-o singură cifră, transformarea îl lasă
nemodificat. Hash-ul se calculează realizând succesiv transformarea asupra
numărului original și apoi asupra rezultatului obținut, de k ori, și sumând
toate rezultatele parțiale și rezultatul final (excluzând valoarea de start).

Cerință
Se dau două numere naturale N şi k și apoi încă N numere naturale. Se cere să
se determine valoarea maximă a hash-ului care se va obține aplicând algoritmul
de hash celor N numere folosind k pentru numărul de iterații de transformare,
conform descrierii de mai sus.

Date de intrare
La intrarea programului se prezintă pe prima linie două numere naturale
N și k, separate prin spațiu.Pe a doua linie se află cele N numere,
separate tot prin spații. Liniile de intrare se încheie cu caracterul newline
(\n), obținut prin apăsarea tastei Enter.

Date de ieșire
Programul va afișa la consolă (pe stream-ul stdout) un singur număr,
reprezentând valoarea maximă dintre toate hash-urile obținute conform
procedeului descris anterior.
ATENŢIE la respectarea cerinței problemei: afișarea rezultatelor trebuie făcută EXACT în 

Restricții
1. 0 < N < 10000
2. 0 ≤ ni < 100000000 (valorile asupra cărora se va aplica hash-ul).
3. 0 < k < 100
'''
N, k = input().split()
N = int(N)
k = int(k)

if N > 0  and N < 10000 and k >0  and k < 100:
    maxim = 0
    n = [0]*N
    n = input().split()
    
    for i in range(len(n)):
        if int(n[i]) >= 0 and int(n[i]) < 100000000:
            suma = 0
            if len(n[i]) == 1:
                recalc = n[i]
            else:
                for j in range(k):
                    recalc = ""
                    for t in range(len(n[i])-1):
                        if int(n[i][t]) > int(n[i][t+1]):
                            dif = int(n[i][t]) - int(n[i][t+1])
                        else:
                            dif = int(n[i][t+1]) - int(n[i][t])
                        recalc += str(dif)
                    suma += int(recalc)
                    n[i] = recalc
                    if suma > maxim:
                        maxim = suma
                   
        else:
            print("Numar incorect!")
            
    print(maxim)
    
else:
    print("Numere introduse incorect!")

