'''
Cărţile din biblioteca UPB trebuie mutate într-o nouă locaţie, iar aranjarea
lor pe rafturi se va face într-o manieră inovativă, urmărindu-se minimizarea
numărului de rafturi necesare. Bibliotecara știe că are un număr suficient de
rafturi încât să pună toate cărțile. Pe fiecare raft încap cărți însumând în 
total D pagini. De asemenea, ştie câte cărţi cu un anumit număr de pagini
există în bibliotecă. Dat fiind acestea şi urmărind să ocupe cât mai puţine
rafturi, bibliotecara şi-a propus să aranjeze cărţile pe rafturi:
    i. raft după raft,
    ii. alegând întotdeauna să completeze raftul curent cu cea mai groasă
        carte disponibilă,
    iii. trecând la următorul raft numai în condiţiile în care pe raftul
        curent nu mai poate fi plasată nicio carte dintre cele rămase şi
    iv. asigurându-se că a plasat pe rafturi toate cărţile.
    
Cerinţă
Scrieţi un program care o poate ajuta pe bibliotecară să aranjeze cărţile pe
rafturi în mod eficient, conform regulilor enunţate mai sus.

Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date:
    • de pe prima linie: două numere întregi D şi k, separate prin spaţiu,
      reprezentând D –dimensiunea rafturilor exprimată în număr de pagini,
      k – numărul de dimensiuni diferite pentru cărţile ce trebuie aranjate în
      bibliotecă;
    • de pe următoarele k linii: câte două numere întregi n şi p, reprezentând
      numărul de cărţi n de grosime p pagini ce trebuie aranjate în bibliotecă.
Cele k linii ce conțin informații despre cărți sunt date în ordinea inversă a
grosimii p.
Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline
(tasta Enter).

Date de ieşire
Programul va afişa pe ecran (stream-ul standard de ieşire) m linii,
corespunzătoare celor m rafturi pe care a fost plasată cel puţin o carte,
în ordinea completării lor (conform regulilor). Fiecare dintre cele m linii va
conţine o serie de numere întregi, separate prin spaţiu, reprezentând
dimensiunile cărţilor ce au fost plasate pe acel raft, în ordinea plasării
lor pe raft (conform regulilor).

Restricţii şi precizări
1. Dimensiunea rafturilor D este număr întreg în intervalul [50; 10000].
2. Grosimile cărţilor p sunt numere întregi în intervalul [1; 1000].
3. Numerele n de cărţi de diverse grosimi sunt numere întregi în intervalul
  [1; 100].
4. Se garantează faptul că nu vor exista cărţi de grosime p mai mare decât
dimensiunea D a rafturilor.
5. Nu este necesar ca rafturile să fie umplute la dimensiunea maximă D.

'''

D,k = input().split()
D = int(D)
k = int(k)

if D >= 50 and D <= 10000:
    n = [0]*k
    p = [0]*k
    nr_carti = 0
    for x in range(0,k):
        n[x],p[x] = map(int, input().split())
        nr_carti += n[x]
        if p[x] < 1 or p[x] > 1000:
            print("Grosime carte incorecta!")
        if n[x] < 1 or n[x] > 100:
            print("Numar de carti incorect!")

    m = [""]*nr_carti
    k = 0
    while k < nr_carti:
        i = 0
        d = D
        while i < len(p):
            if d - p[i] < 0 or n[i] <= 0:
                i += 1
            else:
                d -= p[i]
                m[k] = str(m[k]) + str(p[i]) + " "
                n[i] -= 1
        k += 1
    for x in m:
        print(x)      
            
else:
    print("Dimensiunea rafturilor trebuie sa apartina intervalului [50, 10000].")









