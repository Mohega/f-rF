def factorial(x):
    return x*factorial(x-1) if x>1 else 1
a = int(input("N: "))
d = 1
f = 1
while d != a:
    d = factorial(f)
    f = f + 1
f = f -1 
print(f)
import time
time.sleep(500)
