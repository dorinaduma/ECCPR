'''
Sunteți șef de proiect la o companie și l-ați rugat pe Gigel să dea comandă de
loturi de componente electronice pentru a realiza un set de plăci cu circuite
electronice. Problema este că Gigel nu știe prea multă electronică așa că printre
loturile pe care le-a comandat sunt și loturi cu tranzistoare condensatoare sau
rezistoare insuficiente. Loturile care vă sunt utile sunt doar loturile care au un 
număr de condensatoare mai mare sau egal cu numărul de tranzistoare, numărul de
rezistoare mai mare sau egal cu numărul de condensatoare, și au cel puțin un
condensator, un tranzistor și un rezistor. 
În plus, vă interesează și lotul cu cele mai multe componente, pentru că din ele
o să le mai completați pe cele lipsă.

Cerință
Scrieți un program care primește la intrare loturile de componente și afișează
câte dintre aceste loturi vă sunt utile și câte componente are lotul cel mai
mare. Un lot se consideră util dacă respectă condițiile impuse mai sus.
Aceste condiții trebuie îndeplinite simultan.

Date de intrare
Se va citi de la tastatură (fluxul stdin) pe o singură linie un număr întreg
n reprezentând numărul de loturi. Apoi, se vor citi cele n loturi după cum
urmează: se citește pe o linie numărul de componente din lotul respectiv, k,
iar pe următoarea linie k litere reprezentând tipurile de componente ale
lotului, separate prin spatii (R reprezentând un rezistor, C reprezentând
un condensator și T reprezentând un tranzistor).

Date de ieșire
Programul va afișa pe ecran (stream-ul standard de iesire) două numere întregi,
reprezentând numărul de loturi utile dintre cele citite cât și numărul de
componente ale lotului cel mai mare, valori separate printr-un spațiu.

Restricții și precizări
1. 0 ≤ n < 100
2. 0 ≤ k < 100
'''

n = int(input("Introduceti numarul de loturi: "))

if n >= 0 and n < 100:
    i = 0
    utile = 0
    maxim = 0
    while i < n:
        k = int(input())
        R = 0
        C = 0
        T = 0
        
        if k >= 0 and k < 100:
            if k > maxim:
                maxim = k

            comp = input().split()
            for j in range(k):
                if comp[j] == "R":
                    R += 1
                if comp[j] == "C":
                    C += 1
                if comp[j] == "T":
                    T += 1
            if C >= T and R >= C and R >=1 and C >=1 and T >=1 :
                utile += 1           
        else:
            print("Numarul de componente trebuie sa fie cuprins in intervalul [0, 100).")
        i += 1
    print(utile," ", maxim)         
else:
    print("Numarul de loturi introduse trebuie sa fie cuprins in intervalul [0, 100).")


















