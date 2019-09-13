import sys
import argparse
from fractions import Fraction
import math
 
# This function executes the fractran algorithm
def fractran(n,f):
    if not f:
        print('Fractran program empty')
        return
    else:
        # n in this iteration is the element at the end of n array
        n_upd = n
        print('n this iteration '+str(n[-1]))
        for fraction in f:
            prod = Fraction(n_upd[-1])*fraction
            if prod.denominator == 1:
                n_upd.append(prod.numerator)
                print('nupd = ' + str(n_upd))
                fractran(n_upd,f)
                break
        return n
 
# This function finds the unique prime factorization of n and outputs a list of tuples (prime, # of occurences)
def uniqFact(n):
    # Instantiate list of tuples
    f = []
 
    #Check if i | n
    if n % 2 == 0:
        c_2 = 0
        while n % 2 == 0:
            c_2 += 1
            n = int(n/2)
        f.append(('2', c_2))
    
    if n % 2 != 0:
        # Since n is not divisible by 2, n is odd by the parity property
        # An integer a that is divisible by n cannot be greater than the square root of n
        for i in range(3,int(math.sqrt(n))+1,2):
            c_i = 0
            # Check if i | n
            if n % i == 0:
                while n % i== 0:
                    c_i+=1
                    n = int(n/i)
                f.append((str(i),c_i))
            else: 
            # integer doesn't divide n
                continue
            
        # if the first 2 operations above did not result in 1, n must be prime
        if n > 2:
            f.append((str(n),1))
 
    return f
 
if __name__ == "__main__":
    # Create a parser to read the Fractran program
    parser = argparse.ArgumentParser(description='Run FRACTRAN programs')
    parser.add_argument('filename')
    args = parser.parse_args()
 
    n_in = []
 
    with open(args.filename) as file:
        # Get first line (input)
        firstline = file.readline().replace(' ','');
        
        try:
            # Get the number after IN in the Fractran Program
            n_in = [int(firstline[2:])]
        except ValueError as e:
            print('Invalid fractran syntax. Input should be written as IN # ',e);
            sys.exit(1)
        # Get second line
        secondline = file.readline();
        # Get the fractions from the Fractran program while eliminating any free spaces that might have been added
        fracs = []
        for frac in secondline.replace(' ', '').split(','):
            # Split into numerator, denominator
            fparts = frac.split('/');
            numerator = int(fparts[0])
            denominator = int(fparts[1])
            # Define and add fraction to fracs
            fracs.append(Fraction(numerator,denominator))
            print(fracs)
 
    # Compute prime factorization of the IN number
    print(n_in[0])
    factorization_inn = uniqFact(n_in[0])
    print("Factorization of IN n: " + str(factorization_inn))
 
    # Call fractran
    n_fin = fractran(n_in, fracs)
 
    # Print the list contained n through each iteration
    print('All values of n: '+str(n_fin))
 
    # Compute the factiorization/prime register states of FIN n
    factorization_finn = uniqFact(n_fin[-1])
    print("Factorization of OUT n: "+ str(factorization_finn)) 
