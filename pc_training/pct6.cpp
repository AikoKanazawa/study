#include<iostream>
#include<Eigen/Dense>
#include<Eigen/Eigenvalues>

int main(){

double a,b,c,d,e,f;

	std::cout << "好きな数字6つを入力してください。" << std::endl;
	std::clog << "a,b,c,d,e,f = ?";
	std::cin >> a >> b >> c >> d >> e >> f;

	Eigen::Matrix<double, 3 , 3> A;
	A << a,b,c, b,d,e, c,e,f;

	std::cout << "行列式は" << std::endl;
	std::cout << A << std::endl;

	Eigen::EigenSolver<Eigen::Matrix<double, 3, 3>> s(A);
   	std::cout << "固有値は" << s.eigenvalues() << std::endl;
   	std::cout << "固有ベクトルは" << s.eigenvectors() << std::endl;

	Eigen::ComplexEigenSolver<Eigen::Matrix<double, 3, 3>> ces;
	ces.compute(A);

	Eigen::Matrix<std::complex<double>,Eigen::Dynamic,Eigen::Dynamic> LamA;
	LamA = ces.eigenvalues().asDiagonal();

	std::cout << "行列を対角化すると" << LamA << std::endl;
	
	for (int i=0; i<3; ++i) for (int j=0; j<3; ++j) {
      		if (i == j) {
         		if (abs(LamA(i,i)-s.eigenvalues()(i)) > 1e-12) {
            			std::cout << i << "th eigenvalue is incorrect." << std::endl;
         		}
     	 	} else {
         		if (abs(LamA(i,j)) > 1e-12) {
            			std::cout << i << "(," << j << ") element is incorrect." << std::endl;
         }
      }
   }
}
