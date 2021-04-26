import sys
import math as ma
a1 = int(input('What is the number you would like to get the cosine of? '))
a2 = int(input('How many decimal places would you like the answer rounded to?'))
def cos_degrees(degrees = 0, num_digits = 0):
    cosn1 = degrees*ma.pi/180
    cosn1 = ma.cos(cosn1)
    print('The cosine of {} is {}'.format(degrees, round(cosn1, num_digits)))
cos_degrees(a1, a2)