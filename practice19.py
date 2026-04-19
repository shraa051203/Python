#check perfect number
##num=int(input("Enter the number: "))
##sum=0
##for i in range(1,num):
##    if num%i==0:
##        sum+=i
##
##if sum==num:
##    print("Perfect number:")
##else:
##    print("Not perfect Number:")


#########################
#sum of n natural number
##num=int(input("Enter the number:"))
##sum=0
##for i in range(1, num+1):
##        sum+=i
##
##print(sum)


#sum of integer present inside the list
##lst=[23, "shraa", 45,8,90,"priya"]
##sum=0
##for n in lst:
##    if type(n)== int:
##        sum+=n
##print(sum)

################################################################

##input="hello"
##output={0:"h", 1:"e", 2:"l", 3:"l",4:"o"}

##name="shraddha"
##output={}
##for i in range(len(name)):
##    output[i]=name[i]
##print(output)

################################################################

##get output in form of string and its length
##words={"hai","hello","hii","how","are","you"}
##ans={}
##for word in words:
##    ans[word]=len(word)
##
##print(ans)

############################################
#check given number is prime or not
##n=int(input("Enter the number:"))
##count=0
##for i in range(2,n):
##    if n%i==0:
##        count+=1
##if count==0:
##    print("prime number")
##else:
##    print("Not prime number")
    
##################################################
# print uppercase ulphabet
##for i in range(65,92):
##    print(chr(i))

#pattern question
##num=5
##for i in range(1,num+1):
##    for j in range(i):
##        print("*", end=" ")
##    print()


##num=5
##for i in range(1, num+1):
##    for j in range(i):
##        print(j, end=" ")
##    print()

####################################################

#list of even numbers based on user entered range
##def even_numbers(start,end):
##    return [number for number in range(start, end+1) if number%2==0]
##print(even_numbers(1,50))

####################################################

#factorial
##def fact(num):
##    product =1
##    for i in range(1,num+1):
##        product*=i
##    return product
##print(fact(5))

########################################################################    
#RECURSION

##extract even number from 100 to 1 using recursion
##def write_even(i=100):
##     if i>=1:
##         if i%2==0:
##             print(i)
##         write_even(i=i-1)
##write_even()
##




# Access char of str using recursion

##def use_char(str,i=0):
##    if i< len(str):
##        print(str[i])
##        use_char(str,i=i+1)
##
##use_char("Shraa")


#Extrac integer using recursion
##lst=["shrss", 45,89,90,"hii",89]
##def find_nums(lst, numbers=[], i=0):
##    if i<len(lst):
##        if type(lst[i])==int:
##            numbers.append(lst[i])
##        return find_nums(lst, numbers, i=i+1)
##    return numbers
##
##print(find_nums(lst))        
            

# extract count of vowels from each str

names=["shraa", "aeiou", "deep"]

for name in names:
    count=0
    for i in name:
        if i in "aeiouAEIOU":
            count+=1

    print(name, count)














