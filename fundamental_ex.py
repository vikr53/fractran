from fractions import Fraction
 
def fractran(n, c):
 
    if c <= 20:
        #Print n
        print(n)
 
        #Conway's example used the following fractions
        fractions = [Fraction(17,91), Fraction(78, 85), Fraction(19,51), Fraction(23,38), Fraction(29,33), Fraction(77,29),
        Fraction(95,23), Fraction(77,19), Fraction(1,17), Fraction(11,13), Fraction(13,11), Fraction(15,14),
        Fraction(15,2), Fraction(55,1)];
 
        #Starting with 17/91, the product n*fraction(i) is calculated
        #If a fraction exists such that n*fraction(i) is an integer, n will changed to n*fraction(i) and the function will be
        #called recursively with the updated n
        #If such a fraction does not exist in fractions list, the algorithm halts
        for fraction in fractions:
            prod = Fraction(n)*fraction
            if prod.denominator == 1:
                fractran(prod, c+1)
                break
 
if __name__ =='__main__':
    m = 2
    count = 0;
    fractran(m, count)
