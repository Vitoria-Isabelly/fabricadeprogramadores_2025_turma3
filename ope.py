a=3 
b=2
c=4
d=10
 
A+B= 3+2= 5
D-C= 10-4= 6
A*C= 3*4= 12
D/B= 10/2= 5
D%A= 10%3= 1
(A+B)*C= (3+2)*4= 20
D//B= 10//2= 5 
C*B=4*2= 16 
A+C+D= 3+4+10= 17
D-A*B= 10-3*2= 10-6= 4

A>B = 3>2 = True
C<D = 4<10 = True
A==B = 3==2 = False
D>=C = 10>=4 = True
B<=A = 2<=3 = True
A!= C = 3!=4 = True
(A+B)==C = (3+2)==4 = 5==4 = False
D == 10 = True
C>A = 4>3 = True
B<C = 2<4 = True

(A>B) and (D>C) = True and True = True
(A==B) or (C==4) = False or True = True
not (A==C) = not (False) = True
(B<A) and (C>D) = True and False = False
(D>=10) or (A < 1) = True or False = True
not (D < A) = not (False) = True
(C==4) and (B!=A) = True and True = True
(A==3) or (D==5) = True or False = True
(B<=C) and not (A==D) = True and True =  True
not ((A+B)>D) = not (5>10) = not (False) = True

def media(a, b, c, d):
    return (a + b + c + d) / 4

   
resultado = media(3, 2, 4, 10)
