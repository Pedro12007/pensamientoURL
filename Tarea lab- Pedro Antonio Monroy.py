num = int(input("Ingrese un número: "))

if num <= 99999 and num >= 10000:
    a = num//10000
    b = (num%10000)//1000
    c = (num%1000)//100
    d = (num%100)//10
    e = (num%10)

    ascendente = 0
    descendente = 0
    
    if a >= b and b>=c and c>=d and d>=e:
        print(a,b,c,d,e)
        print(e,d,c,b,a)
    if b>=c and c>=d and d>=e and e>=a:
        print(b,c,d,e,a)
        print(a,e,d,c,b)
    if c>=d and d>=e and e>=a and a>=b:
        print(c,d,e,a,b)
        print(b,a,e,d,c)
    if d>=e and e>=a and a>=b and b>=c:
        print(d,e,a,b,c)
        print(c,b,a,e,d)
    if e>=a and a>=b and b>=c and c>=d:
        print(e,a,b,c,d)  
        print(d,c,b,a,e)
    if a>=c and c>=b and b>=d and d>=e:
        print(a,c,b,d,e)
        print(e,d,b,c,a)
    if b>=a and a>=c and c>=d and d>=e:
        print(b,a,c,d,e)
        print(e,d,c,a,b)
    if c>=a and a>=b and b>=d and d>=e:
        print(c,a,b,d,e) 
        print(e,d,b,a,c)
    if d>=a and a>=b and b>=c and c>=e:
        print(d,a,b,c,e)
        print(e,c,b,a,d)
