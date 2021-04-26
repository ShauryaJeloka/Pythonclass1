import sys

def divis(a):
    print('Larger number is', a[1])
    print('Smaller number is', a[2])
    if int(a[1]) % int(a[2]) == 0:
        print(a[2], "is a factor of", a[1])
    else:
        print(a[2], 'is not a factor of', a[1])
divis(sys.argv)