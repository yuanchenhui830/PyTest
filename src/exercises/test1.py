import numpy as np
import math
def test1():
    """简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？"""
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != j and j != k and i != k:
                    print("输入结果为：%d%d%d"%(i,j,k))
                    
def test2():
    """企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
    奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
    高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，
    可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%，
    高于100万元时，超过100万元的部分按1%提成.
提问：从键盘输入当月利润I，求应发放奖金总数？"""
    a = 123000
    v = 0.0
    arr = [1000000,600000,400000,200000,100000,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    for i in range(0,6):
        if a > arr[i]:
            c = a - arr[i]
            a = arr[i]
            v = v + c * rat[i]
    
    print("结果：%f"%(v))

def test3():
    """简述：一个整数，它加上100和加上268后都是一个完全平方数
提问：请问该数是多少？"""
    add1 = 100
    add2 = 268
    min = np.min(add1,add2)
    c = np.abs(add1 - add2)
    for i in range(0,int((c)/2) + 2):
        for j in range(i,int((c)/2) + 1):
            if (i + j) * (j - i) == c and pow(i,2) >= min:
                print(pow(i,2) - min)
             
def test3_1():
    for i in range(10000):
    #转化为整型值
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))
        if(x * x == i + 100) and (y * y == i + 268):
            print(i)

def test4():
    """简述：要求输入某年某月某日
提问：求判断输入日期是当年中的第几天？"""
    a = [2021,3,1]
    months = (0,31,59,90,120,151,181,212,243,273,304,334)
    ifBig = (a[0] % 400 == 0) or ((a[0] % 4 == 0) and (a[0] % 100 != 0))
    result = months[a[1] - 1] + a[2]
    if(a[1] > 2 and ifBig):
        result += 1
    print(result)
        
def test5():
    """整数顺序排列问题简述：任意三个整数类型，x、y、z
提问：要求把这三个数，按照由小到大的顺序输出"""
    a = [13,25,13]
    b = [13,25,13]
    for i in range(1,len(a)):
        for j in range(i,len(a)):
            if(a[j] <= a[i - 1]):
                a[i - 1],a[j]=a[j],a[i - 1]
    print(a)
    b.sort()
    print(b)

def test6(x): 
    """输出第10个斐波那契数列"""
    if (x == 1) or (x == 2):
        return 1
    else:
        return test6(x-1) + test6(x-2)

def test7():
    """将一个列表的数据复制到另一个列表中。"""
    a = np.arange(10)
    b = [1,2,3,4,5]
    c = b.copy()
    b[0] = 10
    print(a)
    print(c)
    
def test8():
    """话说有一对可爱的兔子，出生后的第三个月开始，每一月都会生一对小兔子。当小兔子长到第三个月后
    ，也会每个月再生一对小小兔子.
    问题：假设条件，兔子都不死的情况下，问每个月的兔子总数为多少？"""
    a1 = 1
    b2 = 1
    for i in range(1,21):
        print("%12ld %12ld" % (a1,b2))
        if (i % 3) == 0:
            print("")
        a1 = a1 + b2
        b2 = a1 + b2
def test8_2(n):
    """太慢了"""
    if n == 1 or n == 2:
        return 1
    else:
        return test8_2(n-1) + test8_2(n-2)
test8()
print(test8_2(40))