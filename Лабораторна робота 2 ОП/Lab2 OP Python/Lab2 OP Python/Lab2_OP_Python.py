#14 Задані дійсні числа x,y,z.З'ясувати чи існує трикутник з такими довжинами сторін.
print("Введіть три довільних значення для сторін ")
x=float(input("Enter x "))
y=float(input("Enter y "))
z=float(input("Enter z "))
if x+y>z and x+z>y and y+z>x and x>0 and y>0 and z>0:
    print("Такий трикутник існує")
else:
    print("Не існує ")