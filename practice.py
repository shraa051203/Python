######WHILE, FOR LOOP#################
###################print even no till 100#################
##num=1
##while num<=100:
##    if num%2==0:
##        print(num,end=",")
##    num+=1

############table#####################
##num=int(input("enter the number"))
##i=1
##while i<=10:
##    print(f"{num}*{i}={num*i}")
##    i+=1

##################sum of n natural number####################
##num= int(input("Enter the number: "))
##i=1
##sum=0
##while i<=num:
##    sum+=i
##    i+=1
##print(sum)

###############wap to print element in list are even or odd########
##lst=[10,20,30,33,13,45,90]
##i=0
##while i<len(lst):
##    if lst[i]%2==0:
##        print(f'{lst[i]} is even')
##    else:
##        print(f'{lst[i]} is odd')
##
##    i+=1

#########even no from 0 to 20 in single line##############
##i=0
##while i<=20:
##    if i%2==0:
##        print(i, end=",")
##    i+=1

############check given number is palindrome or not without type casting
##num=1234543218
##rev= 0
##i=num
##while i!=0:
##    last_digit=i%10
##    rev=rev*10+last_digit
##    i//=10
##if num==rev:
##    print("palindrome")
##else:
##    print("not palindrome")


##########print sum of number collecting start and end from user
##start=int(input("enter the start: "))
##end=int(input("enter end number: "))
##i=start
##sum=0
##while i<=end:
##    sum+=i
##    i+=1
##print(sum)

################sum of list numbers
##lst=[1,2,3,4,5]
##i=0
##sum=0
##while i<len(lst):
##    sum+=lst[i]
##    i+=1
##print(sum)

########wap to extract vowels and digits from string#######
##str="hello world 123 hai"
##i=0
##extract_list=''
##while i<len(str):
##    if str[i].isdigit() or str[i] in 'AEIOUaeiou':
##        extract_list+=str[i]
##    i+=1
##print(extract_list)

########################for loop####################################

###########extract all uppercase vowels
##st="shRAddHa KhArraTMAl"
##upper=''
##for char in st:
##    if char in 'AEIOU':
##        upper+=char
##print(upper)

##################len of given collection without using len function
##collection=eval(input("Enter the input"))
##count=0
##for i in collection:
##    count+=1
##print(f"The length of the collection is {count}")
                
#wap to extract all uppercase, lowercase, digits and spl symbol separately from string

##str="shraDDhAKhaRatMal@#1256&"
##uc,lc,d,ss='','','',''
##for char in str:
##    if char.isupper():
##        uc+=char
##    elif char.islower():
##        lc+=char
##    elif char.isdigit():
##        d+=char
##    else:
##        ss+=char
##print(uc,lc,d,ss)        


#########Wap to count specific character from string###
##char=input("Specify the character to count")
##str=input("Enter the string")
##count=0
##for ch in str:
##    if char==ch:
##        count+=1
##print(count)

#######wap to print 1 to 10 using while and for loop
##i=1
##while i<=10:
##    print(i,end="-")
##    i+=1

##i=1
##for i in range(1,11):
##    print(i)
##    

##########3find factorial of given number
##num=int(input("Enter a number"))
##fact=1
##for i in range(1,num+1):
##        fact*=i
##print(fact)


##########print devices of a number##
##num=int(input("Enter the number"))
##for i in range(1,num+1):
##    if num%i==0:
##        print(i)

########sum of devices excluding that number itself
##num=int(input("Enter the number"))
##sum=0
##for i in range(1,num):
##    if num%i==0:
##        sum+=i
##print(sum)

#####perfect number or not
##num=int(input("Enter the number"))
##sum=0
##for i in range(1,num):
##    if num%i==0:
##        sum+=i
##if sum==num:
##    print("perfect number")
##else:
##    print("not a perfect number")

############multiplication table
##num=int(input("Enter the number"))
##for i in range(1,11):
##    print(f"{num}*{i}={num*i}")

############sum of n natural number
##num=int(input("Enter the number"))
##sum=0
##for i in range(1,num+1):
##    sum+=i
##print(sum)

################sum of all integer present in list
##lst=[10,"apple",6+7j,90,77,True]
##sum=0
##for value in lst:
##    if type(value)==int:
##        sum+=value
##print(sum)

##############rev str without using builtin function
##str="abcd"
##rev=""
##for char in str:
##    rev=char+rev
##print(rev)

###########wap to get following o/p
##str='hello'
##o/p={0:'h',1:'e',2:'l',3:'l',4:'o'}
################################st="hello"
################################op={}
################################for index in range(len(st)):
################################    op[index]=st[index]
################################print(op)




