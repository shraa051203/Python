############################## all prime factors of number- check by odd numbers only 2,3,5,7,9,11,13,15 here if number is divisible by 9 then it will be
##already divided
##import math
##num=int(input("Enter the number:"))
##
##while num%2==0:
##    print("2")
##    num=num//2
###for odd
##for i in range(3,int(math.sqrt(num))+1,2):
##    while num%i==0:
##        print(i)
##        num=num//i
##        
##if num > 2:
##    print(num)


########################################### sum of AP =a,a+d, a+2d,......

##n=int(input("enter the number: "))
##a=int(input("Enter first term: "))
##d=int(input("Enter the common difference: "))
##
##sum=n*(2*a+(n-1)*d)/2
##
##print(sum)


######################################## Gcd
##a=int(input("Enter a number:"))
##b= int(input("Enter a number:"))
##
##while b!=0:
##    a,b=b,a%b
##
##print("GCD:", a)

################################################# lcm
##a=int(input("Enter a number: "))
##b= int(input("Enter the number: "))
##x,y=a,b
##while b!=0:
##    a,b= b,a%b
##    gcd=a
##    
##
##lcm= x*y/gcd
##
##print(lcm)


############find remainder w/o % operator
##14%4=3
##so 4*3=12
##14-12=2=> ans

##n=int(input("Enter a number: "))
##num=int(input("Enter a number: "))
##
##
##d=n//num
##ans=d*num
##remainder=n-ans
##
##print("Remainder: ", remainder)

#########################find sqrt of numm
##n=int(input("Enter the number: "))
##high=n
##low=0
##ans=0
##
##while low<=high:
##    mid=(low+high)//2
##
##    if mid*mid== n:
##        ans= mid
##        break
##    elif mid* mid < n:
##        low=mid +1
##        ans= mid
##    else:
##        high= mid - 1
##
##    
##print("Sqtr(floor value):", ans)

######################################find zeros in factorial
n= int(input("Enter a number:"))
count=0
i=5

while n//i>0:
    count+=n//i
    i*=5

print("Trailing zeros:" ,count)




##n = int(input("Enter a number: "))
##
##count = 0
##i = 5
##
##while n // i > 0:
##    count += n // i
##    i *= 5
##
##print("Trailing zeros in", n, "! =", count)





























