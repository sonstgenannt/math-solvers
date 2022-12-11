import jacobi_solve

import math

def soloStras(n, k):
    if n % 2 == 0 and n != 2:
        return "composite"
    if n == 2:
        return "prime"
    conclusion = "probably prime"
    for a in range(2, n-1):
        x = jacobi_solve.jacobiEval([a,n])%n
        print(x)
        if ( x == 0 or pow(a, int((n-1)/2), n) != x):
            conclusion = "composite"
            
        if k > 0:
            k -= 1
        else:
            return conclusion
    

    return conclusion
        