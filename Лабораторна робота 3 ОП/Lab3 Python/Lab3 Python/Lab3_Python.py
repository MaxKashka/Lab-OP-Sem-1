import math
i=0
b=99999999999
s=0
a=float(input("Введіть степінь точності(рекомендовано від'ємне значення) - ",))
e=10**a
print("Точність ",e)
while math.fabs(b)>=e:
    i+=1
    b=((-2)**i)/math.factorial(i)
    print("Число для перевірки з точністю - ",b)
    s=b+s
    print("Проміжкова сума - ",s)
print("Кінцева сума - ",s)
    




