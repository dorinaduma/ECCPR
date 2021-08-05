'''
George tocmai a învăţat despre sistemul de numeraţie cu bază 2 (sistemul de
numeraţie binar). I se pare interesant şi a inventat jocul PC (permutări
circulare), pe care vrea să îl joace cu prietenul său Armin. George îi
spune lui Armin un număr natural nenul n, scris în baza 10 (sistemul zecimal), 
pe care acesta trebuie să-l transforme în baza 2. Se obţine astfel o
secvenţă de cifre binare (biţi), care trebuie să înceapă cu 1 (primul
bit din stânga în reprezentarea binară a numărului n să fie 1).
Ideea jocului inventat de George a fost aplicarea uneia sau mai multor
permutări circulare asupra scrierii în baza 2 a numărului n. Într-o permutare
circulară, toate cifrele secvenţei date, exceptândo pe ultima, sunt mutate
cu o poziţie spre dreapta, ultima cifră devenind prima.
De exemplu, dacă n=107, scrierea sa în baza 2 este 1101011. Prin permutări
circulare succesive putem obţine, în ordine, secvenţele:
1110101
1111010
0111101
1011110
0101111
...
Fiecare astfel de secvenţă reprezintă transcrierea în bază 2 a unui număr
natural m care are o anumită valoare în baza 10. Lui George jocul nu i
s-ar mai părea așa interesant dacă n-ar reuși să scrie un program care
să determine în locul lui numărul natural m. Ajutaţi-l!
Cerinţă
Să se afle cel mai mare număr natural m, scris în baza 10, a cărui scriere
în baza 2 se poate obține prin una sau mai multe permutări circulare ale
scrierii în baza 2 a numărului n.
Date de intrare
Se va citi de la tastatură (fluxul standard de intrare, stdin) pe o
singură linie, numărul natural nenul n, în baza 10, care respectă
cerinţa din enunţ (primul bit din stânga al reprezentării sale în bază 2 
să fie 1).
Date de ieşire
Programul va afişa la consolă (stream-ul standard de ieşire, stdout),
pe o singură linie, numărul natural m, cu semnificaţia cerută în enunţ.

'''
# introducerea numarului de la tastatura
n = int(input("Introduceti numarul intreg n: "))

# conversia in binar
if (n > 0 and n <= 100000):
    binar = bin(n)
    binar = binar[2:] #se elimina partea cu "0b" din conversia in binar

    # permutarile circulare
    m = n
    l = len(binar) # nr. necesar de permutari este egal cu lungimea numarului
    while l > 0:
        p = binar[-1] + binar[ :-1] #se ia ultima cifra si se pune in fata celorlalte
        zecimal = int(p, 2) #conversia dintr-o baza din dec se face: dec = int(nr, baza)
        if m < zecimal:
            m = zecimal
        l -= 1

    print(m)

else:
    print("Numarul introdus nu apartine intervalului (0, 100000]")



