####Program to calculate the GCD using Euclids Algorithm

def gcd(a, b):
    while (b != 0):
        t = a
        print('assigning a to temporary variable,t = ',t)
        a = b
        print('a = b: ',a," = ",b)
        b = t % b
        print('b = t mod b ->',b)
        print('return a ',a)
    return a

print(gcd(20, 8))
#print(gcd(60, 96))