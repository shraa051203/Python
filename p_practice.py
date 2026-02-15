##for i in range(1,6,2):
##    print(i)
    
# reverse a string, palindrome
##str="abc"
##rev=""
##for i in str:
##    rev=i+rev
####print(rev)
##
##if str == rev:
##    print("palindrome")
##else:
##    print("not")


#largest ele 
##lst=[2,3,8,89,90]
##largest=lst[0]
##
##for i in lst:
##    if i > largest:
##        largest=i
##print("largest",largest)

#extract vowels

##str="shratdiyongewyvhgk,bm,zji"
##for i in str:
##    if i in "aeiouAEIOU":
##        print(i)
##    else:
##        continue


## factorial using recursion
##def fac(num):
##    if num in (1,0):
##        return 1
##    return num*fac(num-1)
##print(fac(5))
    
##fibonacci series
##n=10
##a,b=0,1
##for i in range(n):
##    print(a,end=" ")
##    a,b=b,a+b


##a,b=0,1
##for i in range(15):
##    print(a,end=" ")
##    a,b=b,a+b


# remove duplicates from list
##lst=[2,4,5,6,7,8,7,7,6,5,67,0]
##lst2=[]
##for i in lst:
##    if i not in lst2:
##        lst2.append(i)
##
##print(lst2)


##palindrome number
##num=12321
##rev=0
##i=num
##while i>0:
##    last_digit=i%10
##    rev=rev*10+last_digit
##    i=i//10
##
##if num==rev:
##    print("palindrome")
##else:
##    print("Not palindrome")


##num=12321
##rev=0
##i=num
##while i>0:
##    last_digit=i%10
##    rev=rev*10+last_digit
##    i=i//10
##
##if rev==num:
##    print("Palindrome")
##else:
##    print("Not Palindrome")


## print number in list is even or odd
##lst=[2,4,3,5,67,7,9,66]
##for i in lst:
##    if i%2==0:
##        print(f'{i}is even' )
##    else:
##        print(f'{i} is odd')



num=5
for i in range(1,num+1):
    for j in range(1,i):
        print("*",end=" ")
    print()

num=5
for i in range(1,num+1):
    for j in range(i):
        print(i,end=" ")
    print()

for i in range(1,num+1):
    for j in range(i):
        print(j,end=" ")
    print()


for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


for i in range(num+1):
    for j in range(num-i):
        print("-",end=" ")
    for k in range(i):
        print("* ",end="  ")

    print()







n=8
for i in range(1,n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("* ",end="  ")
    print()

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("* ",end="  ")
    print()


















