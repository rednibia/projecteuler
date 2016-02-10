"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""

productn = 1
productd = 1
for n in range(10, 100):
    for d in range(10, 100):
        num = float(n)
        den = float(d)

        num1 = float(list(str(n))[0])
        num2 = float(list(str(n))[1])

        den1 = float(list(str(d))[0])
        den2 = float(list(str(d))[1])
        #if not(num2 == 0 and dec2 == 0) and not(num1 == num2 and dec1 == dec2) and not(num1 == dec1 and num2 == dec2) and num/den < 1:
        if num / den < 1:
            if not(num % 10 == 0 or den % 10 == 0):
                if num1 == den1:
                    if num2 / den2 == num/den:
                        print num
                        print den
                        productn *= num
                        productd *= den
                if num2 == den2:
                    if num1 / den1 == num/den:
                        print num
                        print den
                        productn *= num
                        productd *= den
                if num1 == den2:
                    if num2 / den1 == num/den:
                        print num
                        print den
                        productn *= num
                        productd *= den
                if num2 == den1:
                    if num1 / den2 == num/den:
                        print num
                        print den
                        productn *= num
                        productd *= den

print
print productn
print productd
