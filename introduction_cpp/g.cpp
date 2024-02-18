#include <iostream>

double sqr(double x)
{
	double x2;

	x2 = x*x;

	return x2;
}

int main()
{
	double ret;

	ret = sqr(1.41421356);

	std::cout << "sqrt(2)^2 = " << ret << std::endl;
}
