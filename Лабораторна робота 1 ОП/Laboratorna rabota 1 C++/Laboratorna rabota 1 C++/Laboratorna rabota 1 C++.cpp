// Laboratorna rabota 1 C++.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <math.h>

int main()
{
	//14 Перевести задане значення кута із радіанної міри в градусну
	double RadB, GradB;
	printf("Enter radians ");
	std::cin >> RadB;
	GradB = RadB * 180 / 3.14159265;
	printf("Get degrees ");
	std::cout << GradB;
	return 0;
}


