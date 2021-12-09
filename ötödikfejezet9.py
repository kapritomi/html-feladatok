def derekszogu_e(a, b, c):
    if a > b and a > c:
        if c*c + b*b == a*a and a*a - c*c == b*b and a*a - b*b == c*c:
            return True
        else:
            return False
    if b > a and b > c:
        if a*a + c*c == b*b and b*b - a*a == c*c and b*b - c*c == a*a:
            return True
        else:
            return False
    if c > b and c > a:
        if a*a + b*b == c*c and c*c - a*a == b*b and c*c - b*b == a*a:
            return True
        else:
            return False
    

print(derekszogu_e(int(input("a")),int(input("b")),int(input("c"))))