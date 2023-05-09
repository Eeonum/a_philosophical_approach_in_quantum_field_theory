from sympy import symbols, Sum, Indexed, lambdify, Array, oo, Product, KroneckerDelta
from sympy.physics.quantum import Ket
import numpy as np

n, m, nu = symbols('n m nu', integer=True)
N = Sum(Indexed('n', nu), (nu, 1, 3))
N_prime = Sum(Indexed('m', nu), (nu, 1, 3))

f = lambdify(n, N)
f_prime = lambdify(m, N_prime)

b = []
n_nu = []
m_nu = []

for nu in range(1, 5):
    arr1 = np.array([nu])
    b = np.concatenate((b, arr1))
    arr2 = Indexed('n', nu)
    arr3 = Indexed('m', nu)
    n_nu = np.concatenate((n_nu, Array(arr2)))
    m_nu = np.concatenate((m_nu, Array(arr3)))

print(f(b))
print(f_prime(b))

ket_n_nu = Ket(n_nu)  # Eqn. (1.1)
ket_m_nu = Ket(m_nu) # Eqn. (1.1)
print(ket_n_nu)
print(ket_m_nu)
#
# expr = KroneckerDelta(n_nu, m_nu)
# # s_can = Product(expr)  # Eqn (1.2)
# print(n_nu)

from qutip import basis, qeye, Qobj


# from qutip import inner

n = 2  # quantum number for state ket1
m = 2  # quantum number for state ket2

ket1 = basis(n, 0)  # state with quantum number n and m=0
ket2 = basis(m, 1)  # state with quantum number m and m=1

print(ket1)
print(ket2)
s_can = Qobj.overlap(ket1, ket2)  # inner product of ket1 and ket2 Eqn(1.2)
delta_nm = qeye(n).matrix_element(basis(n, 0), basis(m, 0))  # Kronecker delta

print("Overlap of ket1 and ket2:", s_can)
print("Kronecker delta for n and m:", delta_nm)

