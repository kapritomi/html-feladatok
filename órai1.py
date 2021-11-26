#1. Írj egy programot, amely 1000-szer kiírja a Szeretjük a Python teknőcöket! mondatot!

print("Szeretjük a Python teknőcöket" *1000)

#3. Írj egy programot, ami a for ciklus használatával az alábbi szöveget írja ki

honapok = ["Az év 1. hónapja Január","Az év 2. hónapja Február","Az év 3. hónapja Március","Az év 4. hónapja Április","Az év 5. hónapja Május","Az év 6. hónapja Június","Az év 7. hónapja Július","Az év 8. hónapja Augusztus","Az év 9. hónapja Szeptember","Az év 10. hónapja Október","Az év 11. hónapja November","Az év 12. hónapja December"]

for x in honapok:
    print(x)

# 4. Tételezzük fel, hogy a teknőcünk Eszti a 0 irányban áll – kelet felé néz. Végrehajtjuk az Eszti.left(3645) utasítást. Mit csinál Eszti és merre néz?

import turtle  
#def vonal(toll,h):
#    for i in range(4):
#        toll.left(3645)
#a = turtle.Screen()
#a.bgcolor("green")
#a.title("vonal")
#toll=turtle.Turtle()
#vonal(toll,50)

# körbe-körbe forog és balra néz

# 5. 

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in xs:
    print(i)

for i in xs:
    print(i*i)

x = 0

for i in range(0, len(xs)):
    x = x + xs[i]

print(x)

osszeg = 1
for i in xs:
    osszeg *=i
    
print(osszeg)


 





















