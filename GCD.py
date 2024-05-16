####Program to calculate the GCD using Euclids Algorithm

def gcd(a, b):
    count = 0
    while (b != 0):
        t = a
        print('assigning value of "a" to temporary variable,t = ',t)
        a = b
        print('a = b: ',a," = ",b)
        b = t % b
        count +=1
        print('b = t mod b ->',b)
        print('return a ',a)
    return a, count
result, iterations = gcd(200,12)
print('GCD is: ', result, ' and loop ran ',iterations, ' times.')
#print('GCD is: ', gcd(90, 96))