'''
Se va dezvolta un program care interpretează o secvenţă de date de intrare,
formată din una sau mai multe linii. Programul parcurge secvenţa de intrare
şi determină dacă fiecare din linii reprezintă un număr de înmatriculare
românesc valid, caz în care afişează linia respectivă în consolă.

Date de intrare
Secvenţa de intrare este formată din linii terminate de caracterul newline
(\n), generat prin apăsarea tastei Enter. Fiecare linie este formată din 3
şiruri de caractere separate de spaţiu. Structura fiecărei linii este
ilustrată generic în cele ce urmează:String1 String2 String3 unde String1,
String2 şi String3 sunt şiruri de caractere a căror structură
va fi descrisă în continuare.

Logica internă
Programul va verifica dacă, luate împreună, cele 3 şiruri de caractere din
fiecare linie reprezintă un număr de înmatriculare valid, folosind
următoarele reguli:
 Valorile valide pentru String1 sunt: AB, AR, AG, B, BC, BH, BN, BT, BV,
BR, BZ, CS, CL, CJ, CT, CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH,
MS, NT, OT, PH, SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN (atenţie: doar
litere mari!)
 String2 e format din 2 sau 3 caractere numerice (numărul de caractere
numerice nu este condiţionat de valoarea String1)
 String3 e format din exact 3 caractere litere mari

Date de ieşire
Programul trebuie să afişeze la ieşire, în consolă (pe stream-ul stdout),
exclusiv liniile de intrare care reprezintă un număr de înmatriculare valid
conform regulilor de mai sus. Liniile ce conţin numere valide nu vor fi
modificate în niciun fel, iar ordinea lor va fi păstrată. Fiecare dintre
liniile afişate va fi terminată de caracterul newline (\n).
'''
x = input()
iesire = ""
while x:
    String1 = x.split()[0]
    String2 = x.split()[1]
    String3 = x.split()[2]
    judet = ["AB", "AR", "AG", "B", "BC", "BH", "BN", "BT", "BV", "BR", "BZ", "CS", "CL", "CJ", "CT", "CV", "DB", "DJ", "GL", "GR", "GJ", "HR", "HD", "IL", "IS", "IF", "MM", "MH", "MS", "NT", "OT", "PH", "SM", "SJ", "SB", "SV", "TR", "TM", "TL", "VS", "VL", "VN" ]
    litere = ["A", "B", "C", "D", "E" , "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    if String1 in judet:
        if String2.isdigit() and len(String2) >= 2 and len(String2) < 4:
            if (String3[0] in litere) and (String3[1] in litere) and (String3[2] in litere):
                iesire += String1 + " " + String2 + " " + String3 + "\n"
    x = input()
    
print(iesire)       
