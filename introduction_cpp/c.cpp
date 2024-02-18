#include <iostream>

int main(int argc, char** argv)
{
std::cout << "The␣number of arguments = " << argc << std::endl;
for (int i=0; i<argc; ++i) {
std::cout << "The argument " << i << " is " << argv[i] << std::endl;
}
}
