# I love you Dad Mark William Watters, uncle Rodney Watters, big bro Tai Truscott
# Charles Truscott Watters. It's my 30th birthday today and I cracked a little problem about an algorithm to find potentially an infinite quotient after converting numbers to arbitrary length strings, but first Knuth's Bisection Search algorithm applied to the Python floating-point and later in x86, x86_64, MIPS and ARM RISC (with the XMM and floating-point registers and flags)

class Number(object):
    def __init__(self, n):
        self.n = n
    def add(self, q):
         """ Adds the first Number object to the second number object """
         a = self.n
         b = q.n
         for x in range(b):
             a += 1
         return a
    def subtract(self, q):
         """ Subtracts the first Number object from the second number object """
         a = self.n
         b = q.n
         for x in range(b):
             a -= 1
         return a
    def multiply(self, q):
         """ Multiplies the first Number object by the second number object """
         a = self.n
         b = q.n
         m = 0
         for x in range(b):
             m += q.n
         return m
    def idivide(self, q):
        """ Divides the first Number object by the second number object to integer value """
        a = abs(self.n)
        b = abs(q.n)
        i = 0
        while a > b:
            a -= b
            i += 1
        return i
    def divide(self, q):
        """ Divides the first Number object by the second number object to arbitrary floating point value """
        a = self.n
        b = q.n
        c = self.idivide(q)
        high = b
        low = 0
        g = (high + low) / 2.0000
        gamma = 0.000000001
        while (abs(round((g + c) * b, 6)) != a):
            print("high: {} low: {} (g + c) * b: {}".format(high, low, abs(round(g + c)) * b))
            if abs(round((g + c) * b, 6)) > abs(round(a)):
                high = g
            elif abs(round((g + c) * b, 6)) < abs(round(a)):
                low = g
            g = (high + low) / 2.0
        return g + c
def Arithmetic():
    Thirteen = Number(13)
    FiftyFive = Number(55)
    # Example of polymorphism in the function invocation next
    tdf = Thirteen.divide(FiftyFive)
    print("Thirteen divided by 55 is: {}\n55 times {} is {}".format(tdf, tdf, 55 * tdf), end='\n')
    print("Charles Truscott on his 30th birthday. Love you Mum, Dad, Tai and MIT and Harvard. Thank you edX executives and staff")

if __name__ == "__main__": Arithmetic()


"""

high: 55 low: 0 (g + c) * b: 1540
high: 27.5 low: 0 (g + c) * b: 770
high: 13.75 low: 0 (g + c) * b: 385
high: 6.875 low: 0 (g + c) * b: 165
high: 3.4375 low: 0 (g + c) * b: 110
high: 1.71875 low: 0 (g + c) * b: 55
high: 0.859375 low: 0 (g + c) * b: 0
high: 0.4296875 low: 0 (g + c) * b: 0
high: 0.4296875 low: 0.21484375 (g + c) * b: 0
high: 0.322265625 low: 0.21484375 (g + c) * b: 0
high: 0.2685546875 low: 0.21484375 (g + c) * b: 0
high: 0.24169921875 low: 0.21484375 (g + c) * b: 0
high: 0.24169921875 low: 0.228271484375 (g + c) * b: 0
high: 0.24169921875 low: 0.2349853515625 (g + c) * b: 0
high: 0.23834228515625 low: 0.2349853515625 (g + c) * b: 0
high: 0.236663818359375 low: 0.2349853515625 (g + c) * b: 0
high: 0.236663818359375 low: 0.2358245849609375 (g + c) * b: 0
high: 0.236663818359375 low: 0.23624420166015625 (g + c) * b: 0
high: 0.23645401000976562 low: 0.23624420166015625 (g + c) * b: 0
high: 0.23645401000976562 low: 0.23634910583496094 (g + c) * b: 0
high: 0.23640155792236328 low: 0.23634910583496094 (g + c) * b: 0
high: 0.2363753318786621 low: 0.23634910583496094 (g + c) * b: 0
high: 0.2363753318786621 low: 0.23636221885681152 (g + c) * b: 0
high: 0.23636877536773682 low: 0.23636221885681152 (g + c) * b: 0
high: 0.23636549711227417 low: 0.23636221885681152 (g + c) * b: 0
high: 0.23636385798454285 low: 0.23636221885681152 (g + c) * b: 0
high: 0.23636385798454285 low: 0.23636303842067719 (g + c) * b: 0
high: 0.23636385798454285 low: 0.23636344820261002 (g + c) * b: 0
high: 0.23636365309357643 low: 0.23636344820261002 (g + c) * b: 0
high: 0.23636365309357643 low: 0.23636355064809322 (g + c) * b: 0
Thirteen divided by 55 is: 0.23636362748220563
55 times 0.23636362748220563 is 12.99999951152131
Charles Truscott on his 30th birthday. Love you Mum, Dad, Tai and MIT and Harvard. Thank you edX executives and staff

[Program finished]


"""