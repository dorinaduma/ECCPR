'''
V-ați hotărât în ultimul moment să mergeți la cinematograf pentru a vedea un
film cu prietenii, dar în același timp vă grăbiți să vă întoarceți acasă cât
mai repede. V-ați interesat de dinainte și ați văzut că filmele care rulează
acum la cinema durează aproximativ același timp. Deci, vă interesează în
principal ca filmul pe care o să îl vizionați să înceapă cât mai repede din
momentul în care ajungeți la casa de bilete, iar, în cazul în care sunt mai
multe filme care încep la ora dorită, să îl alegeți pe cel cu prețul biletului
cel mai mic.

Cerință
Dându-se ora la care ajungeți la cinematograf, scrieți un program care să
selecteze din lista de filme pe cel care respectă cel mai bine dorințele voastre.

Date de intrare
Se vor citi de la tastatură (fluxul stdin) de pe prima linie ora la care ajungeți
la cinema, în format hh:mm, iar de pe a doua linie un număr întreg n reprezentând
numărul de oferte disponibile în programul cinematografului. De pe următoarele n
linii se vor citi datele despre fiecare film din ofertă în formatul:
<oră> <preț> <nume film>
Datele din format vor fi separate prin câte un spațiu. Ora de începere a fiecărui
film va fi tot în formatul hh:mm, prețul va fi un număr întreg fără semn, iar
numele filmului va fi un șir de caractere, el putând fi format din mai multe
cuvinte, dar pentru ușurință, ele vor fi separate prin caracterul cratimă (‘-’).
Fiecare linie se va termina cu un caracter newline (‘\n’).

Date de ieșire 
Programul va afișa pe ecran (stream-ul standard de ieșire) un singur șir de
caractere, reprezentând numele filmului ales, în formatul dat în datele de intrare.

Restricții și precizări
1. 0 < n <= 20
2. Orele se vor încadra în intervalul 00:00 – 23:59. Se garantează faptul că în
programul cinematografului vor fi afișate doar ofertele din ziua respectivă, dar
pot apărea și ore anterioare momentului sosirii la cinematograf. Nu vor exista în
datele de intrare două filme care să înceapă la ora cea mai apropiată de ora la
care ați ajuns și care să aibă același preț pentru bilet. Se garantează, de asemenea,
că niciun film din ofertă nu va începe la ora exactă de sosire a voastră la cinema.
'''
hh,mm = input("Introduceti ora sub forma hh:mm: ").split(":")
if int(hh) < 0 or int(hh) > 23 or int(mm) < 0 or int(mm) > 59 :
    print("Ora introdusa este incorecta!")
n = int(input())
if n > 0 and n <= 20:
    min_hh =  24
    min_mm = 60
    min_pret = 10000000
    film_ales = ""
    for i in range(n):
        x = input()
        ora = x.split()[0]
        pret = x.split()[1]
        nume_film = x.split()[2]
        if ora.split(":")[0] >= hh:
            if int(ora.split(":")[1]) > int(mm) and int(ora.split(":")[0]) < int(min_hh) and int(ora.split(":")[1]) < int(min_mm):
                min_hh = ora.split(":")[0]
                min_mm = ora.split(":")[1]
                min_pret = pret
                film_ales = nume_film
            if int(ora.split(":")[0]) == int(min_hh) and int(ora.split(":")[1]) == int(min_mm):
                if min_pret > pret:
                    min_pret =  pret
                    min_hh = ora.split(":")[0]
                    min_mm = ora.split(":")[1]
                    film_ales = nume_film
        
    print(film_ales)
else:
    print("Numarul de oferte disponibile trebuie sa se afle in intervalul (0, 20].")
