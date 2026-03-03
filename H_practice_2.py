#############################################callable
##a=10
##lst=[2,3,4,5,6]
##st="apple"
##d={'a':1,'b':2,'c':3}
##def greet():
##    return "hello world"
##def greeting(name):
##    return f"hello {name}"
##def add(a,b):
##    return a+b
##def mul(a,b,c):
##    return a*b*c
##
##ref=[]
##ref.append(greet)
##ref.append(a)
##ref.append(st)
##ref.append(d)
##ref.append(greeting)
##ref.append(add)
##ref.append(mul)
##
##for v in ref:
##    if callable(v):
##        print(v)

###########################################comprehension
##v=[expression for item in iterable]
##v=[expression for item in iterable if condition]
##v=[TSB if condition else FSB for item in iterable]
##v=[expression for item in iterable for value in item]


##greet="hello shraddha"
##print([i for i in greet])
##
###even number
##print([i for i in range(1,21) if i%2==0])

#print list of palindromes
##list=["shraa", "oyo","eve","anna","bob","shraddha"]
##print([i for i in list if i==i[::-1]])
##
##
###names which are less than 6 char
##print([i for i in list if len(i)<6])
##
###even len strs
##print([i for i in list if len(i)%2==0])
##
### rev the item if str otherwise keep as it is
##print([data[::-1] if type(data)==str else data for data in list])
##

##a=[1,2,3,4]
##b=[5,6,7,8]
##print([i+j for i,j in zip(a,b)])

###############################################function

##def is_even(num):
##    if num%2==0:
##        return True
##    else:
##        return False
##    
##print(is_even(89890))


##def even_no(start,end):
##    return[i for i in range(start,end+1) if i%2==0]
##
##
##print(even_no(1,50))


#factorial
##def fact(num):
##    product=1
##    for i in range(1,num+1):
##        product*=i
##    return product
##print(fact(12))

#is prime
##def is_prime(num):
##    for i in range(2,num):
##        if num%i==0:
##            return False
##        else:
##            return True
##
##print(is_prime(20))


#perfect num 
##def perfect(num):
##    sum=0
##    for i in range(1,num):
##        if num%i==0:
##            sum+=i
##    return sum==num
##
##print(perfect(27))

    
###############################arguments
#positional argument
##def sts(name,age,id):
##    print(f" hello im {name}, my id {id} and im {age} years old")
##    
##sts("steve",22,202)


#keyword argument
##def details(name,age,id,/,mail,*,no):
##    print(f"hello {name} {age} {id} {mail} {no}")
##
##details("sharddha",22,202,"abc@",no=90)
##


##def mul(*args):
##    return args
##
##print(mul(1,2,3,4,5))
##
##
##def data(**kwargs):
##    return kwargs
##print(data(a=1,c=2))


###############################3Recursion

 
# print even number from 100 to 1
##def num(i=100):
##    if i>=1:
##        if i%2==0:
##           print(i)
##    num(i=i-1)
##num()


#access the char from string
##name="shraddha"
##def shr(name,i=0):
##    if i<len(name):
##        print(name[i])
##        shr(name,i=i+1)
##
##shr(name)


##extract vowels from name
##name="shraddha"
##def find(st,v="",i=0):
##    if i<len(st):
##        if st[i] in "aeiouAEIOU":
##            v+=st[i]
##        return find(st,v,i=i+1)
##    return v
##
##print(find(name))

# extract integers in list
##data=[10,'apple',True,45,3.5]
##def integor(lst,num=[],i=0):
##    if i<len(lst):
##        if type(lst[i])==int:
##            num.append(lst[i])
##        return integor(lst,num,i=i+1)
##    return num
##
##print(integor(data))






























