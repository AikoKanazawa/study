#include <iostream>
#include <cmath>
#include <vector>
#include <random>

typedef std::vector<double> VectorR;

double rand_r()
        {
                std::random_device rnd;
                std::mt19937 mt(rnd());
                std::uniform_real_distribution<> RG(0.0, 1.0);

                return RG(mt);
	}

int main()

{

double x, y;
double a;
double n;

        std::cout << "円の中心を入力して下さい。" << std::endl;
        std::clog << "x, y = ?";
        std::cin >> x >> y;
	std::cout << "(" << x << ", " << y << ")" << std::endl;

        std::cout << "円の半径を入力して下さい。" << std::endl;
        std::clog << "a = ?";
        std::cin >> a;
        std::cout << "半径は" << a << std::endl;

        std::cout << "求めたい円の座標の個数を入力して下さい。" << std::endl;
        std::clog << "n = ?";
        std::cin >> n;

        const double pi = 4.0*atan(1.0);

        VectorR X, Y;
        for (double i=0; i<n; ++i){
		double r = rand_r();
		if (r < 0.5) {
                	X.push_back( x + a*cos(2.0*pi*i/double(n)) );
                	Y.push_back( y + a*sin(2.0*pi*i/double(n)) );
       		}
	}

        for (double i=0; i<X.size(); ++i){
        std::cout << X[i] << " " << Y[i] << std::endl;
        }
}
