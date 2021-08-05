'''
Împreună cu echipa de la firmă ați inventat un nou algoritm de generare de
numere pseudo-aleatoare. 
Pentru a valida că generatorul poate fi folosit în algoritmi criptografici
(cryptographically secure)trebuie să implementați și să rulați o baterie de
teste. Unul din aceste teste verifică numărul de apariții pentru fiecare
secvență posibilă de doi biți: 00, 01, 10 și 11 cât și raportul între numărul
de biți de 0 și de 1. Pentru ca secvența de biți să fie aleatoare, trebuie
ca numărul de apariții pentru fiecare din cele patru perechi să fie
aproximativ egale și în același timp numărul de biți de 0 să fie aproximativ 
egal cu cei de 1. Mai precis, trebuie ca raporturile R1 dintre numărul de
apariții a perechii care apare de cele mai multe ori și numărul de apariții
a perechii care apare de cele mai puține ori, cât și raportul R2 între numărul
de apariții ale celui mai frecvent bit și numărul de apariții ale celui mai
puțin frecvent bit să fie mai mici sau egale cu 110%.

Cerință
Dându-se un număr n reprezentând numărul de biți generat de RNG și secvența
de n biți, să se calculeze raporturile R1 și R2 și să se decidă dacă
generatorul este valid sau nu.

Date de intrare
Pe prima linie se află n, numărul de biți generați. Pe a doua linie se află
o secvență continuă de n biți (valori de 0 sau 1), ne-separați prin spații.

Date de ieșire
Programul va afișa în consolă (pe stream-ul stdout) pe prima linie raporturile
R1 și R2 calculate conform descrierii, valori fracționare cu două zecimale,
separate prin spațiu, iar pe a doua linie valoarea 1 dacă generatorul este
valid sau 0 dacă nu este.
Restricții
2 ≤ n ≤ 10000, n este par
'''

n = int(input("Introduceti numarul de biti: "))
biti = ""
d = {}
one = 0
zero = 0
minim = 5000
maxim = 0


if n >= 2 and n <= 10000 and n%2 == 0:
    i = 0
    print("Introduceti ",n," biti:")
    while i < n:
        x = int(input())
        if x == 0 or x == 1:
            biti += str(x) 
            i += 1
            if x == 0:
                zero += 1
            if x == 1:
                one += 1
        else:
            print("Valorile bitilor sunt de 0 sau 1!")
            break
        
    print("Secventa de biti introdusa este: ",biti)

    i = 0
    while i < len(biti)-1:     
        index = biti[i] + biti[i+1]
        print(index)
        if index in d :
            d[index] +=1
        else :
            d[index] = 1
            
        i += 2
   
    print(one," ",zero)
    R1 = max(d.values())/min(d.values())
    R2 = max(one, zero)/min(one, zero)

    print("%.2f" % R1," ","%.2f" % R2)

    if R1 <= 1.1 and R2 <= 1.1:
        print(1)
    else:
        print(0)
else:
    print("Numarul introdus nu respecta conditiile cerintei!")
