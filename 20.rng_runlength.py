'''
Împreună cu echipa de la firmă ați inventat un nou algoritm de generare de
numere pseudo-aleatoare. Pentru a valida că generatorul poate fi folosit în
algoritmi criptografici (cryptographically secure)trebuie să implementați
și să rulați o baterie de teste. Unul din aceste teste verifică numărul de
apariții pentru secvențe de 1 de diferite lungimi. Pentru ca secvența de
biți generată să fie aleatoare, trebuie ca numărul de apariții pentru
fiecare lungime de secvență de 1 să aibă o anumită distribuție statistică.
Mai precis, trebuie ca numărul de secvențe de un bit 1 să fie mai mare sau
egal decât numărul de secvențe de doi biți 1 care trebuie să fie mai mare
sau egal decât numărul de secvențe de trei biți 1, șamd.

Cerință
Dându-se un număr n reprezentând numărul de biți generat de RNG și secvența
de n biți, să se calculeze numărul de apariții pentru fiecare lungime de
secvență de biți 1 și să se decidă dacă generatorul este valid sau nu.

Date de intrare
Pe prima linie se află n, numărul de biți generați. Pe a doua linie se află
o secvență continuă de n biți (valori de 0 sau 1), ne-separați prin spații.

Date de ieșire
Programul va afișa în consolă (pe stream-ul stdout) pe prima linie o
secvență de numere întregi pozitive, separate prin spațiu, reprezentând
numărul de apariții pentru fiecare lungime de secvență de biți 1, începând
cu numărul de apariții pentru o secvență de un singur bit 1 (delimitat de
biți 0) și terminând cu ultimul număr de apariții nenul. Pe a doua linie
se va afișa valoarea 1 dacă generatorul este valid sau 0 dacă nu este.

Restricții
1. 2 ≤ n < 10000
2. Va exista cel puțin un bit 1 în secvență.
'''
n = int(input())
d = [0]*n
maxim = 0

if n >= 2 and n <= 10000:
    biti = input()
    if len(biti) < n:
        raise Exception(f'Ati introdus mai putine cifre decat n: {n}')
    elif len(biti) > n:
        raise Exception(f'Ati introdus mai multe cifre decat n: {n}')

    i = 0
    contor = 0
    while i < n:
        if int(biti[i]) != 0 and int(biti[i]) != 1:
            raise Exception(f'Bitii introdusi sunt incorecti!')
        if int(biti[i]) == 1:
            contor += 1
            while (i+1) < n and contor != 0:
                if int(biti[i]) != 0 and int(biti[i]) != 1:
                    raise Exception(f'Bitii introdusi sunt incorecti!')
                if int(biti[i+1]) == 0 or (i+1) >= n:
                        d[contor] += 1
                        if contor > maxim:
                            maxim = contor
                        contor = 0

                elif int(biti[i+1]) == 1:
                    contor += 1
                i += 1
            if i+1 == n:
                d[contor] += 1
                contor = 0
                i += 1
        elif int(biti[i]) == 0:
            i += 1

    i = 1
    ok = 1
    while i <= maxim:
        print(d[i], end = " ")
        if d[i] < d[i+1]:
            ok = 0
        i += 1
       
    print("")
    if ok == 0:
        print(0)
    else:
        print(1)
          
    
else:
    print("Numarul introdus nu respecta conditiile cerintei!")
