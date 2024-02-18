#include <iostream>
#include <fstream>
#include <vector>

typedef std::vector<int> VectorI;

int main()
{
	std::fstream fs;

	fs.open("a.txt", std::ios::in); // 入力ストリームとしてオープン
	if (fs.fail()) {
		std::cerr << "cannot open \"a.txt\" !" << std::endl;
		exit(1);
	}

	VectorI data; // サイズ可変配列
	int d;
	for (;;) {
		fs >> d;
		if (fs.eof()) break; // ファイル末尾なら終了
		data.push_back(d);
	}
	fs.close();

	// 読み込んだデータの表示
	for (int i=0; i<data.size(); ++i) {
		std::cout << "i = " << i << ": data = " << data[i] << std::endl;
	}
}
