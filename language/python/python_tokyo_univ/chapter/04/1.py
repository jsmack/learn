#!/usr/bin/python3
def average(score):
    return float( score[0] + score[1] + score[2] ) / 3

def total(scores):
    s = 0
    for i in range(0, len(scores)):
        s = s + scores[i]
    return s

def total2(scores):
    s = 0
    for i in range(len(scores)):
        s = s + scores[i]
    
    return s

def total3(scores):
    s = 0
    for i in scores:
        s = s + i
    
    return s

a = [1,2,5,3]
print(a[1])
print(len(a))
print(float(average(a)))
print(total(a))

import ita
#ita.plot.plotdata(a)

print(total2(a))
print(total3(a))
print([1,2,3] * 3)
print(''.join(['hoge','fuga','wan','hhhh']).count('h'))
