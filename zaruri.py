'''
    Problema 2018.3.1 - Zaruri
    Costică e în vacanță și l-au trimis părinții la țară. Acolo se plictisește
groaznic și căutând prin dulapul bunicului, a dat peste o pungă plină ochi
cu zaruri. Neavând cu cine să joace zaruri, Costică s-a apucat să le clădească, unul peste celălalt, cât de sus a putut. Uitându-se apoi la isprava făcută, i-a venit ideea 
să afle care sunt numerele zarurilor de pe fețele acestora care nu se văd.
Dându-și seama că deși e posibil, e mai complicat, și că el e mai degrabă
leneș decât curios, s-a hotărât să afle doar suma tuturor numerelor de pe
toate fețele zarurilor care nu se văd.

    Cerinţă
Dându-se un număr N de zaruri și valorile de pe fețele vizibile ale zarurilor,
calculați suma tuturor fețelor care nu se văd. Se ignoră ordinea reală a
numerelor pe fețele zarurilor, adică cele 6 numere pot apărea pe zar în orice
aranjament.
'''

N = int(input("Introduceti numarul de zaruri: "))
print("Introduceti fetele vizibile de pe fiecare zar:")
l = []

suma_fete_vizibile = 0
for i in range(0,N):
    l.clear()
    print("Zarul ",i+1)
    if i == 0:
        x = 5
    else:
        x = 4
    for j in range(x):
        elem[j] = int(input())
        suma_fete_vizibile += elem[j]
        l.append(elem)
    print("Zarul ",i+1,": ",l,"\n")

suma_totala = (1+2+3+4+5+6)*N
suma_fete_ascunse = suma_totala - suma_fete_vizibile
print("Suma fetelor care nu se vad este: ",suma_fete_ascunse)
