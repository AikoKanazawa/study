#include <tuple>
#include <iostream>

typedef std::tuple<double,double> Point;

Point pos(double x)
{
	return std::make_tuple(x, 2*x);
}

int main()
{
	double x, y;
	Point z;

	std::tie(x, y) = pos(2.71828);
	z = pos(3.14159);

	std::cout << "x = " << x << ", y = " << y << std::endl;
	std::cout << "z<0> = " << std::get<0>(z) << ", z<1> = " << std::get<1>(z) <<
		std::endl;
}
