#include <iostream>
#include <complex>
#include <string>

typedef std::complex<double> Complex;
typedef std::string String;

int main()
{
Complex z = Complex(1.0, 2.0);
String message = "This is a string.";

std::cout << "z = " << z << std::endl;
std::cout << "message = " << message << std::endl;
}
