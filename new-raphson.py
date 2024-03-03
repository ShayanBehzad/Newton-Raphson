import numpy as np
from math import sin,cos, e, exp

# e ** (-x) - sin(x)
# -e ** (-x) - cos(x)
def newton_raphson():
   f_str = input('Enter the function f(x): ')
   df_str = input('Enter the derivative df(x): ')

   # Convert the strings to lambda functions
   f = eval('lambda x: ' + f_str)
   df = eval('lambda x: ' + df_str)

   x0 = float(input('Enter the initial guess: '))
   ep = np.float64(1e-4) # very small number
   max_iter = 100 # maximum number of iterations
   x1 = 0
   counter = 0
   for i in range(max_iter):
       counter += 1
       x1 = x0 - f(x0) / df(x0)
       if abs(x1 - x0) < ep or abs(f(x1)) < ep:
          break
       x0 = x1

   print('The root of the equation is: %.4f' % x1)
   print("The number of iterations is: %d" % (counter))
# 3 * e**x - 1/x
# 3 * e**x + 1/(x**2)

newton_raphson()