## check if given number is prime
##num=int(input("Enter the number:"))
##for i in range(2,num):
##    count=0
##    if num%i==0:
##        count+=1
##
##if count>=1:
##    print("NOT a prime number")
##else:
##    print(" Prime number")


##write prime number of given range
##start=int(input("Enter the start of range:"))
##end=int(input("Enter the end of range:"))
##for i in range(start,end+1):
##    if i >1:
##        is_prime = True
##
##        for j in range(2,i):
##            if i%j==0:
##                is_prime= False
##                break
##
##        if is_prime:
##            print(i, end=" ")


##find sum of all prime number upto n
##n=int(input("Enter the number:"))
##sum=0
##for i in range(2,n+1):
##    is_prime= True
##    
##    for j in range(2,i):
##        if i%j==0:
##            is_prime=False
##            break
##
##    if is_prime:
##        sum+=i
##
##print(sum)


##find first n prime number














## elif
##num1= int(input("Enter number 1: "))
##num2= int(input("Enter number 2: "))
##
##if num1> num2:
##    print("Number 1 is greater than 2")
##elif num2> num1:
##    print("Number 2 is greater than number 1")
##else:
##    print("Num1 is equal to num2")
##    
    
##check if character is digit, uppercase, lowercase, spl symbol
##a=input("Enter a character:")
##if a.isupper():
##    print("The Character is Uppercase")
##elif a.islower():
##    print("The character is Lowercase")
##elif a.isdigit():
##    print("The character is Digit")
##else:
##    print("it is a symbol")

## check if numver is single, double or three digit
##num=int(input("Enter the number:"))
##if -9 <= num <= 9:
##    print("This is single digit number")
##elif -99 <= num <=99:
##    print("This is double digit number:")
##elif -999 <= num <=999:
##    print("This is three digit number")
##else:
##    print("This is more than 3 digit number")


## find greatest of four digit
##num1=int(input("Enter the number:"))
##num2=int(input("Enter the number:"))
##num3=int(input("Enter the number:"))
##num4=int(input("Enter the number:"))
##
##if num1 > num2 and num1 > num3 and num1> num4:
##    print("num1 is greatest")
##elif num2 > num3 and num3 > num4:
##    print("num2 is greatest")
##elif num3 > num4:
##    print("num3 is gretest ")
##else:
##    print("num4 is gretest")



## check if given character is alphabet or not if alphabet check vowel or not
##char=input("Enter a character:")
##if char.isupper() or char.islower():
##    print("It is alphabet")
##    if char in "aeiouAEIOU":
##        print("char is vowel")
##else:
##    print("It is not a Alphabet")


## check given data is list or not, if list check if have middle value and print
##data=eval(input("Enter the values"))
##if type(data)==list:
##    print("yes given data is list")
##    if len(data)%2!=0:
##        mid=len(data)//2
##        print(f'The middle value for the list is {data[mid]}')
##    else:
##        print("No middle value")
##else:
##    print("Not a list")
##        


#
##given_username="shraddha"
##given_password="shraa@123"
##username=input("Enter the username:")
##if username==given_username:
##    print("correct username")
##    password=input("Enter the password")
##    if password==given_password:
##        print("Login succesfully")
##    else:
##        print("Wrong Password")
##else:
##    print("Wrong username")


#################################################
#print sry 100 times
##for i in range(1,101):
##    print("Sorry")

#####################################################
##i=1
##while i<=100:
##    print("Python")
##    i+=1
#################################################

##print table of given number
##num=int(input("Enter the number"))
##for i in range(1,11):
##    print(f'{num}*{i}={num*i}')

##i=1
##while i<=10:
##    print(f'{num}*{i}={num*i}')
##    i+=1     

###############################################
##palindrome number
##num=12321
##rev=0
##temp=num
##while temp>=1:
##    last_digit=temp%10
##    rev=rev*10+last_digit
##    temp//=10
##
##if rev==num:
##    print("palindrome")
##else :
##    print("Not a palindrome")

###############################################
#extract vowels, digits from string
st="shraddha123ghtd78wlaeiou"
vowels, digits='',''
for ch in st:
    if ch.isdigit():
        digits +=ch
    elif ch in "aeiouAEIOU":
        vowels+=ch
    
print(vowels, digits)





