#include <iostream>

int main()
{
	for (int i=0; i<5; ++i) {
		std::cout << "i = " << i << std::endl;
	}
	int j=0;
	while (j<5) {
		std::cout << "j = " << j << std::endl;
		++j;
	}
	bool flag = true;
	j = 0;
	do {
		if (j>5) {
			flag = false;
		}
		std::cout << "j = " << j << std::endl;
		++j;
	} while (flag);
}
