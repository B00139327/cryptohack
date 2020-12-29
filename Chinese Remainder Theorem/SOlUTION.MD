def CRT(Congruence_equations):
#x传入一个列表，keys代表着模数,items代表余数
        def     gcd(a,b):     #求解最大公约数
                while a!=0:
                    a,b = b%a,a  
                return b
        
        def     findModReverse(a,m):#利用扩展欧几里得算法求模逆
                if gcd(a,m)!=1:
                    return None
                u1,u2,u3 = 1,0,a
                v1,v2,v3 = 0,1,m
                while v3!=0:
                    q = u3//v3
                    v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
                return u1%m
         for p in Congruence_equations.keys():
         		M=Congruence_equations[p]*M
       
        x=0
        for p in Congruence_equations.keys():
                x+=findModReverse(M//p,p)*Congruence_equations[p]*M/p  #CRT
        return int(x%M)    #返回同余方程组的解