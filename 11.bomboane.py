'''
Tuturor copiilor le plac bomboanele, aşa că tatăl lui Andrei îi dă o anumită sumă de bani
în fiecare zi să îşi cumpere bomboane. În zona unde locuieşte Andrei există un singur
magazin de bomboane, iar în fiecare zi se vinde un singur tip de bomboană cu un anumit preţ
şi o anumită aromă. Pe zi ce trece, bomboanele sunt înlocuite cu altele cu alt preţ şi cu 
altă aromă. Andrei cumpără bomboane într-o anumită zi dacă el are destui bani de la tatăl
său şi acest lucru duce la creşterea fericirii lui cu un anumit număr de puncte egal cu
aroma bomboanei. Obligatoriu, dacă are destui bani, el va cumpăra bomboana. El păstrează
toţi banii rămaşi după ce a cumpărat bomboanele pentru a-şi putea cumpăra mai multe
următoarea zi. Dacă el nu are destui bani să îşi cumpere bomboane într-o anumită zi, asta
nu înseamnă că este necesar ca punctele lui de fericire să scadă (evident că nici mai
fericit nu îl vor face). Punctele de fericire vor scădea doar dacă el nu a cumpărat, în
oricare din zilele trecute, cel puţin o bomboană cu o aromă mai bună decât cea din ziua
curentă, pe care nu şi-o permite.

Cerinţă
Dându-se un număr n pozitiv, reprezentând numărul de zile în care băiatul primeşte bani
de la tatăl său, apoi n numere pozitive, reprezentând suma de bani pe care o primeşte
băiatul într-o anumită zi, apoi n perechi de numere pozitive, care reprezintă costul şi
aroma bomboanelor din magazin într-o anumită zi, să se calculeze numărul de puncte de
fericire al lui Andrei. Numărul de puncte de fericire va creşte sau va scădea cu numărul
pozitiv prin care este reprezentată aroma, conform spuselor din enunţ. Presupunem că la
început Andrei avea 0 lei şi 0 puncte de fericire.

Date de intrare
Pe prima linie se află numărul întreg pozitiv n, reprezentând numărul de zile în care
băiatul primeşte bani de la tatăl său, urmat de caracterul newline. Pe următoarea linie
se află n valori întregi pozitive, separate prin whitespace, reprezentând suma de bani
pe care o primeşte băiatul într-o anumită zi, urmate de caracterul newline. Pe următoarele
n linii se află perechi de numere întregi de forma "cost_bomboana aroma_bomboana",
care reprezintă costul şi aroma bomboanelor din magazin în fiecare zi.

Date de ieşire
Se va afişa, pe o singură linie, un singur număr întreg, reprezentând numărul de puncte
de fericire pe care le are Andrei la finalul celor n zile. Linia se va termina
obligatoriu cu un caracter newline ("\n").

Restricţii şi precizări
1. Numărul n este un număr întreg, în intervalul [1, 1000].
2. Suma de bani este un număr întreg, în intervalul [0, 1000].
3. Costul (cost_bomboana) şi aroma (aroma_bomboana) sunt numere întregi,
   în intervalul [0, 1000].
4. Numărul de puncte de fericire de la ieşire va fi un număr întreg, cu semn,
   pe 32 de biţi.
'''
n = int(input())
if n >=1 and n <= 1000:
    suma = input().split(" ")
    puncte_de_fericire = 0
    max_aroma = 0
    i = 0
    while i < n:
        if int(suma[i]) >= 0 and int(suma[i]) <= 1000:
            if i > 0:
                suma[i] = int(suma[i]) + int(suma[i-1])
        else:
            print("Suma este incorecta!")
            break
        
        cost,aroma = input().split()
        cost = int(cost)
        aroma = int(aroma)
        if cost >= 0 and cost <= 1000 and  aroma >= 0 and aroma <= 1000:
            if int(suma[i]) >= cost:
                suma[i] = int(suma[i]) - cost
                puncte_de_fericire += aroma
                if aroma > max_aroma:
                    max_aroma = aroma
            else:
                if aroma > max_aroma:
                    puncte_de_fericire -= aroma
                    
        else:
            print("Date incorecte!")
            break
        i += 1
    print(puncte_de_fericire)
        
else:
    print("Numarul de zile introdus este incorect!")






