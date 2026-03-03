######################## reverse a number
##num= 12343
##n= num
##rev=0
##while n>0:
##    ls=n%10
##    rev=rev*10+ls
##    n=n//10
##
##print(rev)

######################## reverse a string
##st="shraddha "
##rev=st[::-1]
##
##print(rev)


####################fibonacci series
##n=int(input("enter the size of series: "))
##a,b=0,1
##for i in range(n):
##    print(a, end=" ")
##    a,b=b,a+b


####################check prime number
##num=int(input("Enter a number"))
##count=0
##for i in range(1,num+1):
##    if num%i==0:
##        count+=1
##
##if count==2:
##    print("prime number")
##else:
##    print("not a prime number")

########################factorial
##n=int(input("Enter the number"))
##fact=1
##for i in range(1,n+1):
##    fact*=i
##
##print(fact)


###############count vowels in a string
##st="aeiouaaaaeiou"
##count=0
##for i in st:
##    if i in "aeiouAEIOU":
##        count+=1
##
##print(count)

###################interview que
##lst=["shraddha","vidya","aeiou"]
##
##for i in range(len(lst)):
##    count=0
##    for ch in lst[i]:
##        if ch in "aeiouAEIOU":
##            count+=1
##    print(lst[i],count)

#################largest element
##lst=[2,5,77,89,56,798]
##max=0
##for i in lst:
##    if i>max:
##        max=i
##
##print(max)
##    


##########################remove duplicates from list
##lst=[4,4,4,5,6,78,7,8,3,23,3,3,7]
##st=set(lst)
##lst=list(st)
##print(lst)# order not preserved

#to preserve order
##new_lst=[]
##for i in lst:
##    if i not in new_lst:
##        new_lst.append(i)
##
##print(new_lst)
        
###############armstrong number
##num=int(input("enter the number"))
##n=num
##pow=len(str(n))
##sum=0
##while n>0:
##    ls=n%10
##    sum+=ls**pow
##    n=n//10
##
##if sum==num:
##    print("Armstrong number")
##else:
##    print("Not an Armstrong number")
        

####################second largest ele
##lst=input("enter the numbers")

##new=list(map(int,input().split()))
##new=list(set(new))
##new.sort()
##print(new[-2])


####################freq of char in string
##str="shraddha"
##freq={}
##for ch in str:
##    freq[ch]=freq.get(ch,0)+1
##print(freq)

##dictionary.get(key, default_value)


n=int(input())
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")

    print()





