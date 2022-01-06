def fügvény(oldalak):
    if oldalak > 150:
        return True
    else:
        return False   

könyv = input("Könyv címe:")
while könyv:
    oldalak = int(input("Oldalak száma:"))
    fügvény(oldalak)

    if fügvény(oldalak)== True:
        print("A",könyv,"hosszú terjedelmű könyv")
    else:
        print("A",könyv,"rövid terjedelmű könyv")

    könyv = input("Könyv címe:")

