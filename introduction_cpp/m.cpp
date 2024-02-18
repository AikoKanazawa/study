#include <iostream>

int main()
{
	const int N = 5;
	int v[N];

	for (int i=0; i<N; ++i) {
		v[i] = 2*i;
	}

	for (int i=0; i<N; ++i) {
		std::cout << "v[" << i << "] = " << v[i] << std::endl;
	}
}
