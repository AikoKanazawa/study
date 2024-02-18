#include <iostream>
#include <vector>

typedef std::vector<double> Vec;

void f(const Vec& v)
{
	for (int i=0; i<v.size(); ++i) {
		std::cout << "v[" << i << "] = " << v[i] << std::endl;
	}
}

int main()
{
	Vec v(10);
	for (int i=0; i<10; ++i) {
		v[i] = 3.14 * i;
	}

	f(v);
}
