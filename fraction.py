class Fraction:

    def __init__(self, top, bottom):
        hcfnum = gcd(top,bottom)
        self.num = top // hcfnum
        self.den = bottom // hcfnum

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        hcfnum = gcd(newden, newnum)
        newnum = newnum // hcfnum
        newden = newden // hcfnum
        return Fraction(newnum, newden)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        hcfnum = gcd(abs(newden), abs(newnum))
        newnum = newnum // hcfnum
        newden = newden // hcfnum
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        hcfnum = gcd(abs(newnum), abs(newden))
        newnum = newnum // hcfnum
        newden = newden // hcfnum
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        hcfnum = gcd(abs(newnum),abs(newden))
        newnum = newnum // hcfnum
        newden = newden // hcfnum
        return Fraction(newnum, newden)


    def show(self):
        print('The fraction is ', self.num, '/', self.den)


def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a





myFraction = Fraction(3, 5)
myFraction2 = Fraction(4, 5)

sumOf2 = myFraction + myFraction2
sumOf2.show()

multiplyOf2 = myFraction * myFraction2
multiplyOf2.show()

subOf2 = myFraction - myFraction2
subOf2.show()

divOf2 = myFraction / myFraction2
divOf2.show()




