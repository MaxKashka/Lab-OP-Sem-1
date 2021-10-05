//14 Задані дійсні числа x, y, z.З'ясувати чи існує трикутник з такими довжинами сторін.
#include <iostream>
using namespace std;
int main()
{
    double x, y, z;
    //Введите три произвольные числа, который будут задача как длина сторон треугольника
    printf("Enter three arbitrary numbers, which will be the problem as the length of the sides of the triangle \n");
    cout << "Enter x ";
    cin >> x;
    cout << "Enter y ";
    cin >> y;
    cout << "Enter z ";
    cin >> z;
    if (x + y > z && x + z > y && y + z > x && x > 0 && y > 0 && z > 0)
    cout << "Such a triangle exists";
    //Такой треугольник существует
    else
    cout << "Does not exist";
    //Не существует
    return 0;
}

