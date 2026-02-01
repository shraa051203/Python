##################################STRING##########
##st="shraddha chatrulal kharatmal hello world hii welcome to python"
##print(st.upper())
##print(st.lower())
##print(st.swapcase())
##print(st.count('shraddha'))
##print(st.rindex('s'))

##print(st.rfind('a'))
##print(st.isupper())
##print(st.isdigit())
##num="263895"
##print(num.isdigit())

##print(st.startswith('s'))
##print(st.endswith('a'))


##print(st.split())
##print(st.split(',',5))

##s=r"hello\task from pytho\n world"
##print(s)

##s="shraddha"
##age=22
##print(f"hello im {s} and im {age} years old")


################################
####dict={'name':"shraddha",'age':22,'id':88,'height':5.3}
##temp={"delhi":30,"mumbai":34,"pune":20,"banglore":35}

################################FUNCTION ###########
#table
##def table(num):
##    for i in range(1,11):
##        print(f"{num}*{i}={num*i}")
##
##table(19)    

##sum of n natural number
##def sum(num):
##    sum=0
##    for i in range(1,num+1):
##        sum+=i
##    print(sum)
##
##sum(100)

#wap to check elemnets in list are even or odd
##nums=[1,3,4,56,78,66,7,9]
##def is_even(numbers):
##    for i in range(len(numbers)):
##        if numbers[i]%2==0:
##            print(numbers[i],"even")
##        else:
##            print(numbers[i],"odd")
##is_even(nums)


##nums=[8,9,6,7,4,5,2,3]
##def is_even(numbers):
##    for num in numbers:
##        if num%2==0:
##            print(num,"even")
##        else:
##            print(num,"Odd")
##is_even(nums)


###print even number from 1 to 20
##def even():
##    lst=[]
##    for i in range(1,21):
##        if i%2==0:
##            lst.append(i)
##    return lst
##print(even())

# check palindrome or not
##def palin(num):
##    rev=0
##    n=num
##    while n>0:
##        ld=n%10
##        rev=rev*10+ld
##        n=n//10
##    if num==rev:
##        print("palindrome")
##    else:
##        print("not")
##
##palin(7821)

#print sum of numbers collecting start and end from user
##def sumnum(start,end):
##    sum=0
##    for i in range(start,end+1):
##        sum+=i
##    return sum
##
##
##print(sumnum(1,10))


######wap to extract vowels,digits from string
##def extract(str):
##    vowel_digit=""
##    for i in range(len(str)):
##        if str[i].isdigit() or str[i] in 'aeiouAEIOU':
##            vowel_digit+=str[i]
##    return vowel_digit
##print(extract("aeiou shraddajhvfg462974bxhbfhsiwht"))
            
#####print values from list

##def showval():
##    lst=[1,2,3,5,6,7,8,8.90,78,666]
##    for i in lst:
##        print(i)
##showval()

#####extract all uppercase,lowercase, numbers from string
##def extract():
##    upper,lower,digit="","",""
##    str="ShtdfETVDSY4278763dsrgey"
##    for i in str:
##        if i.isupper():
##            upper+=i
##        elif i.islower():
##            lower+=i
##        else:
##            digit+=i
##    return upper,lower,digit
##print(extract())

#######count specify char from userinput
##def countch():
##    char=input("enter the char: ")
##    st="asgtysuijddervgstipmfwqsssssssssssssssxznbccxryop"
##    count=0
##    for i in st:
##        if i==char:
##            count+=1
##    return count
##print(countch())

###print devices of number
##def devices(num):
##    for i in range(2,num-1):
##        if num%i==0:
##            print(i)
##
##devices(50)

##factorial
##def fact(num):
##    factorial=1
##    for i in range(1,num+1):
##        factorial*=i
##    return factorial
##print(fact(5))
        
######perfect number
##def real_no(num):
##    sum=0
##    for i in range(1,num):
##        if num%i==0:
##            sum+=i
##    if sum==num:
##        print(f"{num} is perfect number")
##    else:
##        print(f"{num} is not perfect number")
##
##real_no(6)

####sum of all numbers present inside list
##def sum_num():
##    sum=0
##    lst=[5,5,5,5,True,7+6j,"yes"]
##    for i in lst:
##        if type(i)==int:
##            sum+=i
##    print(sum)
##sum_num()

# reverse a string
##def rev_str():
##    str="anmol"
##    rev=""
##    for char in str:
##        rev=char+rev
##    print(rev)
##
##rev_str()
        
##st="hello"
##char_index={}
##for index in range(len(st)):
##    char_index[index]=st[index]
##print(char_index)
##
##str='shraddha'
##dict={}
##for i in range(len(str)):
##    dict[i]=str[i]
##
##print(dict)
    

###Q
##list=['hello','hai','shraa','kharatmal']
##word_length={}
##for i in list:
##    word_length[i]=len(i)
##
##print(word_length)


##def div():
##    num=int(input('enter the number'))
##    count=0
##    for i in range(1,num+1):
##        if num%i==0:
##            count+=1
##    print(count)
##
##div()

## prime or not
##def is_prime(num):
##    for i in range(2,num):
##        if num%i==0:
##            print("not a prime number")
##    else:
##        print("It is prime number")
##is_prime(7)

##################################BREAK,CONTINUE,PASS
#write only first uppercase character from string 
##st="My birthday on 5th december"
##for i in st:
##    if i.isupper():
##        print(i)
##        break

###smallest divisor of given number rather than 1
##def divisor(num):
##    for i in range(2,num+1):
##        if num%i==0:
##            print(i)
##            break
##divisor(6)

#initial index of given character of given character inside string
##str="shraddha"
##char='a'
##for i in range(len(str)):
##    if str[i]==char:
##        print(i)
##        break

#########printing alphabet upto user entered number
##char=input('Enter the character').upper()
##for ch in range(65,91):
##    print(chr(ch))
##    if char==chr(ch):
##           break


##using while loop
##char=input("Enter the Char: ").upper()
##i=65
##while i<91:
##    print(chr(i))
##    if chr(i)==char:
##        break
##    i+=1


###print alphabet w/o vowels
##for i in range(65,91):
##    if chr(i) in "AEIOU":
##        continue
##    print(chr(i))

##wapt print numbers from 1 to 11 by skipping no 6 and 9
##for i in range(1,12):
##    if i==6 or i==9:
##        continue
##    print(i)
##
##i=1
##while i<12:
##    if i in (6,9):
##        i+=1
##        continue
##    print(i)
##    i+=1

#########################extract data present at odd index
##a=[1,2,3,4,5,6,"shraa","hai"]
##odd_index_items=[]
##for i in range(len(a)):
##    if i%2==0:
##        continue
##    odd_index_items.append(a[i])
##print(odd_index_items)
##        


# run the loop continuosly until user enter correct password
##Saved_password='pysp112'
##while True:
##    pwd=input("Enter the Password:")
##    if pwd==Saved_password:
##        print("Login successful")
##        break
##    else:
##        print("wrong password Try again")

#wapt guess the number and pass suggestion
##n=45
##while True:
##    a=int(input("Enter the number:"))
##    if a==n:
##          print("The number is perfect:")
##          break
##    elif a>n:
##        print("Enter number less than this Number")
##    else:
##        print("enter number greater then this number:")
        



    
