#include <iostream>
#include <fstream>

int main()
{
	std::fstream fs;

	fs.open("a.txt", std::ios::out);
	if (fs.fail()) {
		std::cerr << "cannot open \"a.txt\" !" << std::endl;
		exit(1);
	}

	fs << "This is a string." << std::endl;
	fs << "sample text." << std::endl;

	fs.close();
	fs.open("a.txt", std::ios::in);

	std::string str;
	std::getline(fs, str);
	std::cout << str << std::endl;
	std::getline(fs, str);
	std::cout << str << std::endl;
}
