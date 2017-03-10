class Fraction(object):
    """
    A number represented as a fraction
    """

    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
        self.reduce()

    def reduce(self):
        if (self.num == self.denom):
            self.num = 1
            self.denom = 1
            return

        low_value = min(self.num, self.denom)
        high_value = max(self.num, self.denom)
        common_denom = low_value
        count = 1
        done = False

        while not done and common_denom >= 1:
            if high_value % common_denom == 0:
                done = True
            else:
                count += 1
                common_denom = low_value / count
                while common_denom % 1 != 0 and common_denom >= 1:
                    count += 1
                    common_denom = low_value / count

        if done:
            self.num = int(self.num / common_denom)
            self.denom = int(self.denom / common_denom)

    def __str__(self):
        """ Retunrs a string representation of self """
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num * other.denom - self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num / self.denom

    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)


a = Fraction(1, 4)
b = Fraction(5, 4)
c = a + b  # c is a Fraction object
d = b - a
e = Fraction(15, 250)
print('c =>', c)
print('d =>', d)
print('e =>', e)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
