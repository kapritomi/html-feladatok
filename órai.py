#1. Tárold el a Lustaság fél egészség. mondat minden szavát külön változóban, majd jelenítsd meg egy sorba a print függvény használatával.
a = "Lustaság"
b = "fél"
c = "egészség"

print(a +" "+ b +" "+ c)

#2. Zárójelezd úgy a 6 * 1 - 2 kifejezést, hogy a 4 helyett -6 legyen az értéke.
a = 6 * (1 -2)
print(a)

#3. Tegyél megjegyzés jelet egy olyan sor elé, amely korábban már m ˝uködött. Figyeld meg, mi történik, amikor újra futtatod a programot!

#4. Indítsd el a Python értelmezot, és gépeld be a ˝ Pista + 4 kifejezést, majd üss egy Entert. Az alábbi hiba jelenik meg: NameError: name 'Pista' is not defined Rendelj olyan értéket Pista változóhoz, hogy a Pista + 4 kifejezés értéke 10 legyen.
pista = 6
print(pista +4)

#5. Írj programot, amely meghatározza, mennyi lesz egy betét értéke a futamido végén, ha 10000 Ft-t helyezünk betétbe 8%-os névleges kamatláb mellett. Az évközi kamatozások száma (m) 12. Az évek számát, vagyis a t értékét a felhasználótól kérje be a program
C = 100000
r = 0.08
m = 12
t = int(input("Évek száma:"))
FV = C * (1 + r/m)**(m*t)
print(FV)

#6. Jelenleg pontosan 14 óra van. Beállítunk egy ébresztoórát úgy, hogy 51 órával kés ˝ obb csörögjön. Hány órakor fog az ébresztoóra megszólalni? (Segítség: Ha túlzottan vonz a lehet őség, hogy az ujjaidon számold ki, akkor 51 helyett dolgozz 5100-zal.)


nap = 14 + 51
resz = nap % 24  
print(resz)

#7. Írj egy Python programot az eloő feladat általános megoldására. Kérd be a felhasználótól az aktuális időt (csak az órákat) és azt, hogy hány órával késobb szólaljon meg az ébresztőóra, majd jelenítsd meg a képernyőn, hogy hány órakor fog megszólalni az ébresztőóra.

ido = int(input("az időt:"))
idozito = int(input("idozito:"))
idoo = ido + idozito
resz1 = idoo % 24
print(resz1)



