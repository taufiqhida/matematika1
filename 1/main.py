import numpy as np
import scipy.linalg as la
import sympy as sp
sp.init_printing()

#2
#Contoh Matriks 3*3
A = np.array([1,2,3,4,5,6,7,8,9]).reshape((3,3))
# print(A)

#Untuk menukar baris i dengan j di sebuah matriks
#matriks T memiliki elemen yang samadengan matriks identitas
#kecuali Tii = 0, Tjj = 0, Tij =1, Tji = 1

#3
#Menukar baris dengan perkalian matriks T
T = np.eye(3)
T[1, 1] = 0
T[2, 2] = 0
T[1, 2] = 1
T[2, 1] = 1
# print(T)

#Operasi matriks T dari sebelah kiri pada A untuk mennukar baris

T@A

#5
#Sedangkan Operaasi dari sebelah kanan untuk menukar kolom

A@T

#6
#Definisikan Fungsi
#Modifikasi dari ref 1
# Menukar baris i dengan j

def swap_row(A, i, j):
    n= A.shape[0] #menentukan jumlah baris
    E = np.eye(n)
    E[i,j] = 0
    E[j,j] = 0
    E[i,j] = 1
    E[j,i] = 1
    return E @ A

#7

# Buat matriks yang berisi
# baris i dari matriks A
# di tempatkan pada baris j

def get_row(A,i,j):
    n = A.shape[0]
    E = np.zeros((n,n))
    E[j,i] = 1
    return E@A

#8
#Kalilan skala s pada baris i dari matriks A

def scale_row(A, i, s):
    n = A.shape[0]
    E = np.eye(n)
    E[i,i] = s
    return E @ A

#9
swap_row(A, 1,2)

#10
get_row(A,1,2)

#11
scale_row(A, 0, 3)

#12
#Dari persWamaan di atas di peroleh
A = np.array([[2, 3, -1], [1, -2, 1], [3, 1, 2]])
b= np.array([[2], [5], [1]])
# print(A)
# print(b)

#12
#Dari persWamaan di atas di peroleh
A = np.array([[2, 3, -1], [1, -2, 1], [3, 1, 2]])
b= np.array([[2], [5], [1]])
# print(A)
# print(b)

#13 Membuat matriks Augmented
B = np.hstack([A, b])
# print(B)

#14 
# Proses Eliminasi
# ingat indeks mulai dari 0
B = B -(1/2)*get_row(B, 0, 1)
B = B -(3/2)*get_row(B, 0, 2)
# print(B)

#15

B = B - get_row(B, 1, 2)
# print(B)

#16 PROSES SUBSTITUSI
B = scale_row(B, 2, 1/2)
# print(B)

#17

B = B - 1.5*get_row(B, 2, 1)
# print(B)

#18
B = scale_row(B, 1,1/(-3.5))
# print(B)

#19
B = B - 3*get_row(B, 1, 0) + get_row(B, 2, 0)
# print(B)

#20
B = scale_row(B, 0, 1/2)

#21
#Kolom terakhir adalah solusi sistem persamaan linier
# print(B)

#22
#Dengan menggunakan Modul Scipy.limalg
x = la.solve(A, b)
# print(x)

#23
A2 = sp.Matrix(A)
b2 = sp.Matrix(B)
x2 = A2.solve(b2)
# print(x2)

#24 
A=sp.Matrix([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])
# print(A)

#25

# A.elementary_row_op('n->kn', n=0, k=5) 
A.elementary_row_op('n->kn', 0, 5)

#26

# 
A.elementary_row_op('n<->m',1, 2)

#27

#Notes A.elementary_row_op('n->n+km, n=0, k=1, m=2)
A.elementary_row_op('n->n+km', 0, 1, 2)
# print(A)

#28

A = np.array([[2, 3, -1],[1, -2, 1], [3, 1, 2]])
b = np.array([[2],[5],[1]])
B = sp.Matrix(np.hstack([A, b]))
# print(B)

#29

B2 = B.elementary_row_op('n->n+km', 1, -(1/2), 0)
# print(B2)



#30

B3 = B2.elementary_row_op('n->n+km', 2, -(3/2), 0)
# print(B3)

#31

B4 = B3.elementary_row_op('n->n+km', 2, -1, 1)
# print(B4)

#32
B5 = B4.elementary_row_op('n->kn', 2, 1/2)
# print(B5)

#33
B6 = B5.elementary_row_op('n->n+km', 1, -1.5, 2)
# print(B6)

#34
B7 = B6.elementary_row_op('n->kn', 1, 2/7)
# print(B7)

#35
B8 = B7.elementary_row_op('n->n+km', 0, 1, 2)
# print(B8)
B9 = B8.elementary_row_op('n->n+km', 0, 3, 1)
# print(B9)


# Metode Jacobi
#36

tol = 1.0E-10 #toleransi
delta = 1000
xn = 0.0
yn = 0.0
zn = 0.0
n = 0

while delta > tol:
    n += 1
    # xn+1 = F9(xn)
    xnp1 = (1/4.0)*(1.0 - yn + zn)
    ynp1 = -(1/5.0)*(3.0 - xn - zn)
    znp1 = (1/2.0)*(2.0 - xn - yn)
    delta = abs(xnp1 - xn) + abs(ynp1 - yn) + abs(znp1 - zn)
    # Simpan untuk iterasi berikutnya
    xn = xnp1
    yn = ynp1
    zn = znp1

    #  print([n, xn, yn, zn])


#37

tol = 1.0E-10 #Toleransi
delta = 1000 #
xn = 0.0
yn = 0.0
xn = 0.0
n = 0
while delta > tol:
    n += 1
    # xn+1 = F(xn)
    xnp1 = (1/4.0)*(1.0 - yn + zn)
    ynp1 = -(1/5.0)*(3.0 - xnp1 - zn)
    znp1 = (1/2.0)*(2.0 - xnp1 - ynp1)
    delta = abs(xnp1 - xn) + abs(ynp1 - yn) + abs(znp1 - zn)
    # Simpan untuk itelarasi
    xn = xnp1
    yn = ynp1
    zn = znp1

    # print([n, xn, yn, zn])


#38
# Dengan menggunakan Modul Scipy.linalg
# Dari persamaan di atas di peroleh
A = np.array([[4, 1, -1], [1, -5, 1],[1, 1, 2]])
b = np.array([[1], [3], [2]])
X = la.solve(A, b)

# print(x)


#39
# Dengan menggunkan Modul Sympy.solve
A2 = sp.Matrix(A)
b2 = sp.Matrix(b)
x2 = A2.solve(b2)
# print(x2)

