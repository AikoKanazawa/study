#include <iostream>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

typedef Matrix<double,Dynamic,1> EVectorR;
typedef Matrix<double,Dynamic,Dynamic> EMatrixR;

int main()
{
   EMatrixR M(3,3);
   M << 0.0, 1.0, 0.0,
        1.0, 0.0, 1.0,
        0.0, 1.0, 0.0;

   SelfAdjointEigenSolver<EMatrixR> es(M, EigenvaluesOnly);
   EVectorR lam = es.eigenvalues();

   for (double t=0.001; t<5.0001; t+=0.001) {
      double z = 0.0;
      for (int i=0; i<3; ++i) z += exp(-lam(i)/t);
      double e = 0.0;
      for (int i=0; i<3; ++i) {
         double ei = lam(i);
         e += ei * exp(-ei/t);
      }
      e /= z;
      double c = 0.0;
      for (int i=0; i<3; ++i) {
         double ei = lam(i);
         c += ei*ei * exp(-ei/t);
      }
      c /= z;
      c = (c - e*e)/t/t;

      cout << t << " " << e << " " << c << endl;
   }
}

