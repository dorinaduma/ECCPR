'''
Centrul de meteorologie dintr-o ţară nordică doreşte să stabilească modul în
care încălzirea globală influenţează variaţiile de temperatură ale acelei
ţări. Meteorologii notează pe parcursul a N zile consecutive temperaturile
maxime zilnice şi sunt interesaţi să determine cea mai lungă perioadă de 
timp în care temperaturile înregistrate în zile consecutive au alternat ca
semn, precum și statistica valorilor pozitive vs. negative de pe parcursul
celor N zile.

Cerinţă
Scrieţi un program care, pe baza temperaturilor înregistrate pe parcursul a
N zile consecutive, determină o secvenţă de zile având lungime maximă, pentru
care temperaturile înregistrate au alternatca semn. Dacă există mai multe
astfel de secvenţe, meteorologii sunt interesaţi de cea mai recentă. 
Dacă nu există măcar două zile consecutive cu temperaturi alternante ca semn,
ei vor înregistra rezultatul 0, neavând date suficiente pentru calcule
suplimentare. În plus, meteorologii sunt interesați și de procentul valorilor
pozitive și negative înregistrate pe parcursul celor N zile.

Date de intrare
De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N,
reprezentând numărul total de zile pentru care se efectuează studiul.
Pe cea de-a doua linie se prezintă N numere întregi separate prin spaţii,
al i-lea număr de pe linie reprezentând temperatura maximă înregistrată în
ziua i a studiului (1 ≤ i ≤ N).

Date de ieşire
La ieşire (fluxul stdout) pe prima linie se afişează numărul natural NrMax,
reprezentând numărul maxim de zile consecutive pentru care temperaturile au
alternat ca semn. Pe cea de a doua linie vor fi scrise NrMax valori întregi,
separate prin spaţii, reprezentând temperaturile (alternante ca semn)
înregistrate în cele NrMax zile. Dacă există mai multe secvenţe cu acelaşi
NrMax, va fi afişată cea mai recentă dintre acestea. Pe ultima linie se
afișează procentele, calculate cu două zecimale exacte prin rotunjire,
aferente valorilor negative și pozitive de temperatură identificate pe
parcursul celor N zile, în felul următor: +:AB.CD% -:EF.GH%
Aceste procente se calculează ca raport între numărul valorilor pozitive sau
negative și totalul valorilor înregistrate. Afişarea se face cu două zecimale
exacte prin rotunjire. Nu se va face completarea cu 0 dacă partea întreagă a
procentului calculat conține o singură cifră.În cazul în care nu există măcar
două zile consecutive cu temperaturi alternante ca semn, la ieşire se va
afişa o singură linie, pe care va fi scrisă valoarea 0. Nici o altă afişare
nu va mai fi făcută în acest caz. Toate valorile afișate sunt urmate de
caracterul linie nouă (‘\n’) obținut prin apăsarea tastei Enter.

Restricţii şi precizări
1. 3 < N ≤ 365
2. Valorile temperaturilor sunt numere întregi din intervalul [-50, 50].
3. Temperatura de 0 grade va fi considerată pozitivă
'''
N = int(input())

if N > 3 and N <= 365:
    x = [0]*N
    x = input().split()
    negative = 0
    pozitive = 0
    NrMax = 0
    contor = 0
    secvMax = ""
    secv = ""
    j = 0
    for i in range(N):
        if int(x[i]) < 0:
            negative += 1
        else:
            pozitive +=1
            
    for i in range(N-1):
        if (int(x[i]) >= 0 and int(x[i+1]) < 0) or (int(x[i]) < 0 and int(x[i+1]) >= 0):
            if secv == "":
                secv += x[i] + " " + x[i+1] + " "
                contor += 2
            else:
                secv += x[i+1]+ " "
                contor += 1
        else:
            if contor >= NrMax:
                NrMax = contor
                secvMax = secv
            contor = 0
            secv = ""
    if NrMax == 0:
        print(0)
    else:
        print(NrMax)
        print(secvMax)
    print("+:","%.2f" % round((pozitive/N)*100,2),"%", " -:","%.2f" % round((negative/N)*100,2),"%")
else:
    print("Numar de zile introdus incorect!")















