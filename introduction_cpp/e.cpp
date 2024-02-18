#include <iostream>

int main()
{
int a;
std::clog << "a = ? "; std::cin >> a;

 if (a > 10) {
	std::cout << "a is more than 10." << std::endl;
 } else if (a < 0) {
	std::cout << "a is negative." << std::endl;
 } else {
	std::cout << "a is less than 10 and positive." << std::endl;
 }
}
