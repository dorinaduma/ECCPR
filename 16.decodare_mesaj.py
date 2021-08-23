'''
Aţi fost angajaţi la o companie de telecomunicaţii deoarece ei recepţionează
în fiecare zi mesaje de la o sursă necunoscută. Mesajele sunt formate doar
din cifre şi v-aţi dat seama că mesajele au fost codate folosind un cifru
simplu. Mesajul original era format din majusculele limbii engleze, fiecare
dintre acestea fiind convertite într-un număr, folosind următoarea
corespondență:
• A → 1
• B → 2
• ...
• Z →26
Din moment ce mesajul apare ca un șir de cifre neîntrerupte, există multe
moduri în care ar putea fi decodat, dar cei care le transmit s-au gândit
la următorul scenariu:
• Când următoarele două cifre din mesaj pot fi interpretate ca un număr de
două cifre pe care îl putem decoda, le vom interpreta astfel, ignorând
posibilitatea interpretării unei singure cifre.
• Dacă pe poziţia curentă se află un 0, secvenţa 0x se va interpreta ca x,
unde x este orice cifră între 1 şi 9, iar cifra x se va decoda ca atare.
(Exemplu: 01 → 1 → A).
• Două cifre de 0 consecutive vor fi decodate ca un spațiu.

Cerinţă
Să se decodeze mesajul, folosind scenariul de mai sus.

Date de intrare
Pe o singură linie se va citi un şir de cifre neîntrerupte, reprezentând
mesajul codat.

Date de ieşire
Se va afişa, pe o singură linie, mesajul decodat. Linia se va termina
obligatoriu cu un caracter newline ("\n").

Restricţii şi precizări
1. Mesajul va avea maxim 10240 de caractere.
2. Se garantează că mesajul de la intrare este unul valid, adică va conţine
doar cifre
'''
sir = str(input())
sir = [x for x in sir]
litere = [" " , "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
if len(sir) <= 10240:
    mesaj_decodat = ""
    i = 0
    while i < len(sir):
     
        if i+1 < len(sir):
            concat = sir[i] + sir[i+1]
        if (int(concat) > 0 and int(concat) <= 26) or int(concat) == 0:
            mesaj_decodat += litere[int(concat)]
            i += 2
        else:
            mesaj_decodat += litere[int(sir[i])]
            i += 1
    mesaj_decodat += "\n"    
    print(mesaj_decodat)
            
else:
    print("Lungimea sirului introdus este prea mare!")











