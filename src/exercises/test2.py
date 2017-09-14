def test1():
    L = [1,2,3,4,5]
    """列表生成式"""
    s1 = ','.join(str(n) for n in L)
    print(s1)

def test2():
    a = [1 ,2,3,4,5]
    N = len(a) 
    print(a)
    for i in range(int(len(a) / 2)):
        """多元相等"""
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print(a)

a,b=1,2
print(b,a)
test2()

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 =[s.lower() for s in L1 if isinstance(s, str)]
print(L2)