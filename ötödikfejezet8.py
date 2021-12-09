def derekszogu_e(a, b, c):
    if a*a + b*b == c*c and c*c - a*a == b*b and c*c - b*b == a*a:
        return True
    else:
        return False

print(derekszogu_e(int(input("a")),int(input("b")),int(input("c"))))