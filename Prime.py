import random
import time

# 函数：查找质因数。
# 说明：方法简单暴力但是效率低下，如果质因数较小，效率较高。如果存在大质因数，分解效率低下。
#      从2开始的自然数，挨个试：
#      如果：可以合数可以被这个自然数整除，那么这个自然数就是这个合数的质因数
#           然后，用合数除以（整除）这个自然数之后，继续寻找下一个自然数。
#      否则：试下一个自然数。（自然数+1)
# 备注：此方法效率低的原因是把所有奇数自然数作为因数来验证，其中会做很多无用功
def findPF(v: int) -> list:
    n = 2
    l = []
    while n <= v:
        if v % n == 0:
            l.append(n)
            v = v//n
        else:  # 本来== 2:，else 可以直接写 n += 1，但是为了稍微提高一点效率排除2之后所有偶数
            if n == 2:
                n += 1
            else:
                n += 2
    return l

# 函数：查找最大公因数。
# 说明：根据公因数的定义，查找两个数的最大公因数。
#      从2开始直到两个数中较小的数进行查找，
#      如果这个数可以同时被两个数整除，就这两个数的公因数。
def gcd_ricky(a: int, b: int)-> int:
    if a > b:
        s = b
    else:
        s = a
    c = 1
    for i in range(2, s+1):
        if a % i == 0 and b % i ==0:
            c = i
    return c

# 函数：查找最大公因数。
# 说明：根据公因数的定义，查找两个数的最大公因数。
#      ricky的改进，倒序查找，只要找到一个公因数就结束退出。
def gcd_ricky2(a: int, b: int)-> int:
    if a > b:
        s = b
    else:
        s = a
    c = 1
    for i in range(s+1, 1, -1):
        if a % i == 0 and b % i ==0:
            c = i
            break
    return c


# 函数：求两个数的最大公约数。
# 说明：使用欧几里得算法（辗转相除法）求最大公约数
#      1，a除以b 余数为r
#      2，如果r==0，那么b是a,b 的最大公约数
#      3，否则让a=b, b=r,执行步骤1
# 备注：采用递归写法，代码简单，效率较低
def gcd_dad(a: int, b: int) -> int:
    r = a % b
    if r == 0:
        return b
    else:
        return gcd_dad(b, r)

# 函数：求两个数的最大公约数。
# 说明：使用欧几里得算法（辗转相除法）求最大公约数
#      非递归调用写法
def gcd_dad2(a: int, b: int) -> int:
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


if __name__ == '__main__':

    # ------------------效率测试--------------------------BEG
    lst1 = []
    lst2 = []
    cnt = 1000
    for i in range(cnt + 1):
        lst1.append(random.randint(100, 10000))
        lst2.append(random.randint(100, 10000))

    t1 = time.time()
    for i in range(cnt + 1):
        x = lst1[i]
        y = lst2[i]
        a = gcd_dad(x, y)
    t2 = time.time() - t1
    print(f'[dad1]函数找{cnt}对数字的最大公因数耗时{t2}秒')

    t1 = time.time()
    for i in range(cnt + 1):
        x = lst1[i]
        y = lst2[i]
        a = gcd_dad2(x, y)
    t2 = time.time() - t1
    print(f'[dad2]函数找{cnt}对数字的最大公因数耗时{t2}秒')

    t1 = time.time()
    for i in range(cnt + 1):
        x = lst1[i]
        y = lst2[i]
        a = gcd_ricky(x, y)
    t2 = time.time() - t1
    print(f'[rky1]函数找{cnt}对数字的最大公因数耗时{t2}秒')

    t1 = time.time()
    for i in range(cnt + 1):
        x = lst1[i]
        y = lst2[i]
        a = gcd_ricky2(x, y)
    t2 = time.time() - t1
    print(f'[rky2]函数找{cnt}对数字的最大公因数耗时{t2}秒')
    # ------------------效率测试--------------------------END


    '''
    num = input('求两个数的最大公因数，请输入两个整数，用空格分开：')
    lst_input = num.split(' ')
    x = int(lst_input[0])
    y = int(lst_input[1])
    lst = findPF(x)
    s = f'{x}={"*".join(str(j) for j in lst)}'
    lst = findPF(y)
    s = s + f';     {y}={"*".join(str(j) for j in lst)}'
    print(s)
    
    
    z = gcd_ricky(x,y)
    print(f'[嘟嘟1]:{x}和{y}的最大公因数是{z}; 最小公倍数是{x*y//z}')
    z = gcd_ricky2(x,y)
    print(f'[嘟嘟2]:{x}和{y}的最大公因数是{z}; 最小公倍数是{x*y//z}')
    z = gcd_dad(x,y)
    print(f'[爸爸1]:{x}和{y}的最大公因数是{z}; 最小公倍数是{x*y//z}')
    z = gcd_dad2(x,y)
    print(f'[爸爸1]:{x}和{y}的最大公因数是{z}; 最小公倍数是{x*y//z}')
    '''

    '''
    num = int(input('输入你想要分解的正整数:'))
    lst = findPF(num)
    s = f'{num}={"*".join(str(i) for i in lst)}'
    print(s)
    '''


    '''
    for i in range(2, 201):
        lst = findPF(i)
        s = f'{i}={"*".join(str(j) for j in lst)}'
        print(s)
    '''