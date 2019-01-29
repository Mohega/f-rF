import time
def factorial():

    

    
    n = input("Number (factorial:  ")
    q = 0
    r = 1
    a = len(n)
    n = n.replace(" ", "")
    
    d = [a+b for a,b in zip(n[::2], n[1::2])]
    print (d)
    
    for i in d:
        i = int(i)
        for l in range (1,i):
                i = l * i
                print(i)
        d[q] = i
        q = q + 1 

    
    
    print("Completed")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    
    print(d)
    
def factorialiser(x):
    return x*factorialiser(x-1) if x>1 else 1
    
def rFList():
    l = input("List, reverse factorial  ")
    list1 = l.split(", ")
    print (list1)
    list2 = []
    
    for i in list1:

       
        a = int(i)
        d = 1
        f = 1
        while d != a:
            d = factorialiser(f)
            f = f + 1
        f = f -1 
        print(f)

        print (f)
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print (d)
        list2.append(f) 
    print(list2)

        
def rFactorial(n):      
    
    x = 2
    while n != 1:
        n = n/x

        x = x+1
        
    print("completed")
    x = x -1
    return(x)
    




choice = input ("F or rF")
if choice == 'F':
    factorial()
elif choice == 'rF':
    rFList()
else: print("no")

time.sleep(600)
