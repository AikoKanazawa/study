#include <iostream>
#include <fstream>

int main()
{
	const int N = 5;
	std::fstream fs; // ファイルストリーム

	fs.open("a.txt", std::ios::out); // 出力ストリームとしてオープン
	if (fs.fail()) {
		std::cerr << "cannot open \"a.txt\" !" << std::endl;
		exit(1);
	}

	for (int i=0; i<N; ++i) {
		fs << 10*i << std::endl;
	}

	fs.close();

	fs.open("a.txt", std::ios::in); // 入力ストリームとしてオープン

	int data[N];
	for (int i=0; i<N; ++i) {
		fs >> data[i];
		std::cout << "i = " << i << ": data = " << data[i] << std::endl;
	}

	fs.close();
}
