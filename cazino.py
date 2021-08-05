'''
Un faimos cazino din București dorește să detecteze mai rapid trișorii de la
mesele lor de cărți. Folosind un program de recunoaștere a imaginilor se pot
detecta ce cărți sunt jucate de fiecare jucător de la masă și se dorește să
se descopere dacă vreunul din ei a scos cărți din buzunar. Jocul monitorizat 
se joacă cu două pachete clasice (52 de cărți fiecare, fără Joker).
Cerință
Scrieți un program care să ajute la detectarea trișorilor. În cazul în care
se detectează că o carte apare de prea multe ori, programul va afișa cartea
și va opri jocul.

Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date:
• Pe prima linie se află numărul n, reprezentând numărul maxim de mâini
ce vor fi jucate;
• Pe următoarele n linii se află cartea jucată, în formatul:
<număr_carte> <semn_carte>

Date de ieşire
În cazul în care nimeni nu încearcă să trișeze se va afișa textul JOC OK.
În cazul în care cineva a încercat sa trișeze, se va afișa cartea problemă
în același format ca la intrare: numărul cărții urmat de semn, separate
prin spațiu.

Restricții și precizări
1. 2 < n < 100
2. Semnul carţilor poate fi: trefla, caro, cupa, pica. 
3. Numărul cărților este un număr întreg în intervalul [2; 14] (asul e notat 11).
'''
n = int(input())

if ( n > 2 and n < 100 ):
    x = {} #folosim un dictionar pentru indexare deorarece poate avea index si str
    prima = 0
    i = 0
    while i < n :
        nr_carte, semn_carte = input().split()
        if int(nr_carte) < 2 or int(nr_carte) > 14 or semn_carte not in ["trefla","cupa","caro","pica"]:
            print("Valori incorecte!")
            break;     
        i += 1
        index = nr_carte+" "+semn_carte

        if index in x :
            x[index] +=1
        else :
            x[index] = 1
            
        if x[index] == 3 and prima == 0:
            prima = 1
            failed = index

    if prima == 0 :
        print("JOC OK")
    else:
        print(failed)

else :
    print("Numarul introdus nu apartine intervalului (2, 100).")

# Timp de lucru: 60 de minute
