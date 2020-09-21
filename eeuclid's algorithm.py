#euclid's algorithm


class algorithms:
    def eculids_algorithm(self):
        a = int(input('a= '))    #give input1
        b = int(input('b= '))    #give input2
        if (a==0) and (b==0) :
            print(' invalid input')
        else:
            if a<0:
                a= (0-a)
            if b<0:
                b= (0-b)           # change in sign do not change gcd.

            # x = q1*y +Z
            x = max(a,b)
            y = min(a,b)           #write  a,b in order

            if y==0:
                print('gcd('+str(a)+','+str(b)+') = '+str(x))  #special case:if one of a,b is zero
            else:
                z=x%y
                if z==0:
                    print('gcd('+str(a)+','+str(b)+') = '+str(y))  #case; if y is divisor of x
                else:
                    while z!=0:     # for other general cases
                        z0=z
                        x=y
                        y=z
                        z=x%y
                    print('gcd('+str(a)+','+str(b)+') = '+str(z0))
                    print('''
                    
                    ''')



    def Euclids_algorihm_Extended(self):

        # Rn = x*s + y*t
        a = int(input('a= '))       #give input1
        b = int(input('b= '))       #give input2
        if (a == 0) and (b == 0):
            print(' invalid input')
        else:
            if a < 0:
                a = (0 - a)
            if b < 0:
                b = (0 - b)          # change in sign do not change gcd.

            # Rn = x*s + y*t
            x = max(a, b)
            y = min(a, b)

            if y == 0:
                print('gcd= '+str(x))
                print('minimal pair of Bezout coefficients is' + str(1) + ',' + str(0) + '.')
                print(str(x) + ' = ' + str(x) + '*' + str(1) + ' + ' + str(y) + '*' + str(0))       #special case:if one of a,b is zero
            else:
                s0, t0 = 1, 0
                s1, t1 = 0, 1
                r0, r1 = x , y

                while True:
                    q = (r0 // r1)
                    r = (r0 % r1)   #(r = r0 - q*r1)
                    s = (s0 - q*s1)
                    t = (t0 - q*t1)

                    if r == 0 :
                        print('gcd =' + str(r1))
                        print('minimal pair of Bezout coefficients is' + str(s1) + ',' + str(t1) + '.')
                        print('')
                        print(str(r1)+' = '+str(x)+'*'+str(s1)+' + '+str(y)+'*'+str(t1))
                        break
                    else:
                        r0, s0, t0 = r1, s1, t1
                        r1, s1, t1 = r , s , t






A=algorithms()

A.eculids_algorithm()

A.Euclids_algorihm_Extended()









