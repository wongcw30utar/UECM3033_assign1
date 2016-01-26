import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(3*sy.cos(2*x))* sy.sin(2*x), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[1,3,7,8,1,1,1,1,5,4],
                   [2,1,3,7,8,8,2,9,4,5],
                   [5,8,1,3,7,2,8,4,9,8],
                   [6,5,-3,1,2,4,7,8,1,9],
                   [7,6,5,2,1,3,4,7,8,1],
                   [9,7,6,5,4,1,3,6,7,2],
                   [3,2,4,6,5,9,1,3,6,7],
                   [8,9,2,4,6,5,9,1,3,6],
                   [1,4,8,1,9,6,5,2,1,3],
                   [4,1,9,9,3,7,6,5,2,1] ] )
                   
    b = np.array( [3,2,4,2,1,9,7,1,3,4] )
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1203938
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
