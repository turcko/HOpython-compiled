import ctypes as C
math = C.CDLL('./addyarray.so')


print("Ejemplos de enteros y puntos flotantes:")
print("------------------------------------------\n")

# probando float add_float(float a, float b)
a = 3.5
b = 4.6

math.add_float.restype = C.c_float	
math.add_float.argtypes = [C.c_float, C.c_float]

print("Probando --> [float add_float(float a, float b)] con  valores %f y %f: %f" % (a,b, math.add_float(a,b)))

# probando int add_int(int a, int b)
a = 3
b = 4

math.add_float.restype = C.c_int	
math.add_float.argtypes = [C.c_int, C.c_int]

print("\nProbando --> [int add_int(int a, int b)] con valores %d y %d: %d" % (a,b, math.add_int(a,b)))
# int add_float_ref(float *a, float *b, float *c)
a = C.c_float(3.8)
b = C.c_float(4.5)
resultado = C.c_float()
math.add_float_ref(C.byref(a),C.byref(b), C.byref(resultado))
print("\nProbando --> [int add_float_ref(float *a, float *b, float *c)] con valores %r y %r: %r" % (a,b, resultado.value))

# int add_float_ref(float *a, float *b, float *c)
a = C.c_int(3)
b = C.c_int(4)
resultado = C.c_int()
math.add_int_ref(C.byref(a),C.byref(b), C.byref(resultado))
print("\n Probando --> [int add_int_ref(int *a, int *b, int *c)] con valores %r y %r: %r" % (a,b, resultado.value))
print("\n------------------------------------------")

print("\n\nEjemplos de arreglos:")
print("------------------------------------------\n")

print("SIN NUMPY\n")

dim = 3
print("\nProbando suma\n")
arre1 = (C.c_int * 3) (1, 2, -5)
arre2 = (C.c_int * 3) (-1, 3, 3)
resultado = (C.c_int * 3) (0,0,0)
math.add_int_array(C.byref(arre1), C.byref(arre2), C.byref(resultado), dim)

arregloSuma = []
sumando1 = []
sumando2 = []
for i in range(0,dim):
    sumando1.append(arre1[i])
    sumando2.append(arre2[i])
    arregloSuma.append(resultado[i])
print("%r + %r = %r" %(sumando1, sumando2, arregloSuma))

print("\nProbando producto\n")
dim = 3
arre1 = (C.c_float * 3) (1, 2, -5)
arre2 = (C.c_float * 3) (-1, 3, 3)
resultado = C.c_float()
resultado = math.dot_product(C.byref(arre1), C.byref(arre2), dim)

factor1 = []
factor2 = []
arregloProducto = []

for i in range(0,dim):
    factor1.append(arre1[i])
    factor2.append(arre2[i])

# NO FUNCA BIEN, MUESTRA RESULTADO ERRONEO!!!!!!!!!!!!!!!!
print("%r * %r = %.2f" %(factor1, factor2, resultado))

print("\nCON NUMPY\n")
import numpy as np

intp = C.POINTER(C.c_int)
arre1 = np.array([1, 2, -5], dtype=C.c_int) #elementos del arreglo a tipo entero de C
arre2 = np.array([-1, 3, 3], dtype=C.c_int)
resultado = np.zeros(3, dtype=np.float16)
math.add_int_array(arre1.ctypes.data_as(intp), arre2.ctypes.data_as(intp), resultado.ctypes.data_as(intp), C.c_int(3)) #arre1.ctypes.data_as(intp) puntero a entero de C
print(resultado)


print("\n------------------------------------------")