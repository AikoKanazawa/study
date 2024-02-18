#include <iostream>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_multiroots.h>


using namespace std;


struct rparams {
   double a, b;
};


// the Rosenbrock system of equations, f0(x,y) = a(1-x), f1(x,y) = b(y-x^2).
int rosenbrock_f(const gsl_vector* x, void* params, gsl_vector* f)
{
   rparams* p = reinterpret_cast<rparams*>(params);
   double a = p->a;
   double b = p->b;

   double x0 = gsl_vector_get(x, 0);
   double x1 = gsl_vector_get(x, 1);

   double y0 = a * (1 - x0);
   double y1 = b * (x1 - x0 * x0);

   gsl_vector_set(f, 0, y0);
   gsl_vector_set(f, 1, y1);

   return GSL_SUCCESS;
}


void write_status(int iter, gsl_multiroot_fsolver* s)
{
   cout << "iter = " << iter
      << ", x = " << gsl_vector_get(s->x, 0)
      << ", y = " << gsl_vector_get(s->x, 1)
      << ", f0(x,y) = " << gsl_vector_get(s->f, 0)
      << ", f1(x,y) = " << gsl_vector_get(s->f, 1)
      << endl;
}


int main()
{
   // parameters, a, b.
   rparams p = { 1.0, 10.0 };
   size_t n = 2;

   // set function.
   gsl_multiroot_function f = { &rosenbrock_f, n, &p };

   // set argument.
   double xi[2] = { -10.0, -5.0 };
   gsl_vector* x = gsl_vector_alloc(n);
   gsl_vector_set(x, 0, xi[0]);
   gsl_vector_set(x, 1 ,xi[1]);

   // generate solver.
   const gsl_multiroot_fsolver_type* T = gsl_multiroot_fsolver_hybrids;
   gsl_multiroot_fsolver* s = gsl_multiroot_fsolver_alloc(T, n);
   gsl_multiroot_fsolver_set(s, &f, x);

   // output header.
   int iter = 0;
   write_status(iter, s);

   // solver loop.
   int max_iter = 1000;
   double eps = 1e-7;
   int status;
   do {
      ++iter;
      status = gsl_multiroot_fsolver_iterate(s);
      write_status(iter, s);
      if (status) break;
      status = gsl_multiroot_test_residual(s->f, eps);
   } while (status == GSL_CONTINUE && iter < max_iter);

   cout << "status = " << gsl_strerror(status) << endl;

   gsl_multiroot_fsolver_free(s);
   gsl_vector_free(x);
}


