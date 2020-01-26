def bmi(height, weight):
    return weight / height  ** 2

def misseard(tf, h):
    tc = (tf - 32) / 1.8
    return (tc - 0.4 * (tc - 10) * ( 1 - h / 100))

print ('BMI', bmi(170.0,100.0))
print misseard(60,88)

import math
print(math.cos(3.14))