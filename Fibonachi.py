def fib(n):
    saraksts=[]
    a=0
    b=1
    while a<n:
        saraksts.append(a)
        temp_var=b
        b=a+b
        a=temp_var
    print (saraksts)

fib(10000)
