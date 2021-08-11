'''
Costică e în vacanță și l-au trimis părinții la țară. Acolo se plictisește
groaznic și căutând prin dulapul bunicului, a dat peste o pungă plină ochi
cu zaruri. Neavând cu cine să joace zaruri dar părându-i-se că unele din
zaruri sunt mai grele decât celelalte, Costică a ales un zar și s-a apucat
să îl testeze aruncând cu el și notând de câte ori a picat fiecare față.
Încearcă apoi să-și dea seama dacă zarul e măsluit sau nu, considerând că
diferența dintre numărul maxim de apariții a unei fețe și numărul minim de
apariții (a oricăror alte fețe) nu trebuie să depășească 10% din numărul
total de aruncări.

Cerinţă
Dându-se un număr N de aruncări cu zarul și apoi N numere naturale în
intervalul [1:6] reprezentând numerele obținute la aruncări, să se determine
dacă zarul e măsluit conform condiției de mai sus.

Date de intrare
De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N,
reprezentând numărul de aruncări cu zarul. Pe următoarele N linii se află
câte un număr natural în intervalul [1:6] reprezentând numerele obținute la
aruncări.

Date de ieşire
La ieşire (fluxul stdout) se va afișa un singur număr, 0 sau 1, 0 dacă zarul
e normal, și 1 dacă este măsluit.

Restricţii şi precizări
1. 10 ≤ N ≤ 100
'''
N = int(input("Introduceti numarul de aruncari: "))

if N >= 10 and N <= 100:
    d = {}
    i=1
    while i <= 6:
        d[i]= 0
        i += 1
    ten_percent = 0.1 * N

    for i in range(N):
        x = int(input())
        if x > 6 and x < 1 :
            print("Numarul introdus trebuie sa apartina intervalului [1, 6].")
            break
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    maxim = max(d.values())
    minim = min(d.values())

    if (maxim - minim) <= ten_percent:
        print(0)
    elif (maxim - minim) > ten_percent:
        print(1)
else:
    print("Numarul de aruncari trebuie sa apartina intervalului [10, 100].")
