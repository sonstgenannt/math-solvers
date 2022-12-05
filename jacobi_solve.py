import math

def twosym(j):
    J = pow(-1, (pow(j[1], 2)-1)/8)
    return J

def sepsym(j):
    
    comp = [j]
    
    s = 1
    if j[0] < 0:    s = -1
    
    if j[0] == 2:
        return twosym(j)
    if abs(j[0]) % 2 == 0:
        comp = ([(2, j[1]),(j[0]/2, j[1])])
    else:
        return j
    
    n = 1
    while len(comp) > 1:
        j = [i*twosym(comp[0]) for i in comp[1]]
        comp = [j]
        #print(j)
        
        if j[0] == 2:
            return twosym(j)
        if abs(j[0]) % 2 == 0:
            comp = ([(2, j[1]),(j[0]/2, j[1])]);    n +=1
        else:
            print("dividing out 2**" + str(n))
            return j

def flipsym(j):    ## QUADRATIC RECIPROCITY    
    if abs(j[0]) < abs(j[1]) and abs(j[0]) %2 != 0 and abs(j[0]) != 1:
        J = [i*pow(-1, (abs(j[0])-1)*(abs(j[1])-1)/4) for i in (j[1], j[0])]
    else:
        return j
    
    """
    J = (j[1], j[0])
    if (j[0] % 4 == 1 or j[1] % 4 == 1):
        return J
    if (j[0] % 4 == j[1] % 4 == 3):
        J = [-i for i in J]
    """
    
    return J

def modsym(j):
    s = 1
    if j[0] < 0:    s = -1
    
    if abs(j[0]) != 1:
        J = (s*(abs(j[0])%abs(j[1])), s*(abs(j[1])))
    else:
        return s
    return J

def jacobiEval(j):
    stages = [j]
    if math.gcd(j[0], j[1]) != 1:
        return 0
    print(type(j))
    
    methods = [[flipsym, "flip"], [sepsym, "separate 2**n"], [modsym, "modulo"]]
    
    while type(j) == tuple or type(j) == list:
        for m in methods:
            if j not in [-1,0,1]:
                J = m[0](j)
                if (type(J) != float and type(J) != int and list(J) != list(j)):    print (m[1],":", J)
                j = J
    return j
