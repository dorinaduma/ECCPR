'''
Clasamentul echipelor ce participă la un campionat de fotbal se realizează
întotdeauna pe baza rezultatelor meciurilor disputate între echipele
participante. Fotbalul se joacă pe goluri, astfel că o echipă este declarată
câştigătoare dacă înscrie mai multe goluri decât cealaltă. Dacă ambele echipe 
înscriu la fel de multe goluri, meciul este declarat remiză. Este cunoscut
faptul că o victorie se punctează cu 3 puncte, o remiză cu un punct, iar în
cazul unei înfrângeri echipa în cauză nu primeşte niciun punct. La finalul
campionatului, echipele sunt ordonate în funcţie de numărul de puncte
acumulate, cea cu cele mai multe puncte câştigând trofeul.

Cerinţă
Stabiliţi clasamentul final al campionatului de fotbal pe baza rezultatelor
directe între echipele participante.

Date de intrare
Se vor citi de la tastatură (fluxul stdin) următoarele date: 
 o valoare întreagă k reprezentând numărul de echipe participante, urmată
   de caracterul newline (tasta Enter);
 o valoare întreagă n reprezentând numărul de meciuri disputate în campionat,
   urmată de caracterul newline (tasta Enter);
 n linii reprezentând rezultatele celor n meciuri disputate, în următorul
   format:
<Nume echipa 1> <Numar goluri echipa 1> – <Numar goluri echipa 2> <Nume echipa 2>
Entităţile componente ale liniilor reprezentând rezultate sunt separate
printr-un spaţiu, ca în exemplul dat în final. Fiecare dintre cele n linii
reprezentând rezultate este urmată de caracterul newline (tasta Enter).

Date de ieşire
Programul va afişa pe ecran (stream-ul standard de ieşire), lista de k echipe
participante, sortată în ordinea numărului de puncte. Fiecare dintre cele k
linii va avea formatul de mai jos (între entităţile componente fiind câte un
spaţiu, ca în exemplul dat în final):
<Nume echipa> <Numar puncte> <Numar goluri inscrise> < Numar goluri primite>

Restricţii şi precizări
1. Numele echipelor nu conţin alte caractere în afară de a,b,…,z şi A,B,…,Z.
2. Garantăm faptul ca nu vor exista echipe cu acelaşi număr de puncte
'''
k = int(input())
n = int(input())
d = {}

for i in range(n):
    e1, goluri_e1,line, goluri_e2, e2 = input().split()
    if e1 in d:
        d[e1][1] += int(goluri_e1)
        d[e1][2] += int(goluri_e2)
        if int(goluri_e1) > int(goluri_e2):
            d[e1][0] += 3
        elif int(goluri_e1) == int(goluri_e2):
            d[e1][0] += 1
    else:
        d[e1] = [0,0,0]
        d[e1][1] = int(goluri_e1)
        d[e1][2] = int(goluri_e2)
        if int(goluri_e1) > int(goluri_e2):
            d[e1][0] = 3
        elif int(goluri_e1) == int(goluri_e2):
            d[e1][0] = 1
    if e2 in d:
        d[e2][1] += int(goluri_e2)
        d[e2][2] += int(goluri_e1)
        if int(goluri_e2) > int(goluri_e1):
            d[e2][0] += 3
        elif int(goluri_e2) == int(goluri_e1):
            d[e2][0] += 1
    else:
        d[e2] = [0,0,0]
        d[e2][1] = int(goluri_e2)
        d[e2][2] = int(goluri_e1)
        if int(goluri_e2) > int(goluri_e1):
            d[e2][0] = 3
        elif int(goluri_e2) == int(goluri_e1):
            d[e2][0] = 1
            
d = dict(sorted(d.items(), key = lambda x: x[1],reverse = True))
for i in d:
	print(i,end = " ")
	for j in d[i]:
		print(j,end = ' ')
	print('')






