import numpy
x = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
y = [1,   6,  17,  34,  57,  86, 121, 162, 209, 262, 321]
coeffs = numpy.polyfit(x,y,deg=2)
print(coeffs)
