from fractions import Fraction as F

#ouput: 2/3
print(F(1,3)+F(1,3))

#ouput: 6/5
print(1 / F(5,6))

#ouput True
print(F(-3,10) < 0)