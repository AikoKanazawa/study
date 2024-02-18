#include <iostream>
#include <vector>

typedef std::vector<int> Vec;

void outputV(const Vec& v)
{
	std::cout << "--- size = " << v.size() << std::endl;
	for (int i=0; i<v.size(); ++i) {
		std::cout << "v[" << i << "] = " << v[i] << std::endl;
	}
	std::cout << "-----" << std::endl;
}

int main()
{
	Vec v;

	v.push_back(3);
	v.push_back(2);
	v.push_back(4);

	outputV(v);

	v.resize(8);
	for (int i=0; i<v.size(); ++i) {
		v[i] = 3*i;
	}

	outputV(v);
}
