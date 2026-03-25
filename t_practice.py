## prime number
##num=int(input("enter number to check"))
##if num<=1:
##    print("It is not a prime number")
##else:
##    for i in range(2,num):
##        if num%i==0:
##            print("Not a prime number")
##            break
##    else:
##            print("It is a prime number")


#########################################################

##palindrome num
##num=int(input("enter a number"))
##temp=num
##rev=0
##while num>0:
##    ls=num%10
##    rev=rev*10+ls
##    num=num//10
##
##if rev==temp:
##    print("palindrome")
##else:
##    print("Not a Palindrome")

#############################################################

## sum of digits
##num=int(input("Enter a number"))
##temp=num
##sum=0
##while temp>0:
##    ls=temp%10
##    sum=sum+ls
##    temp=temp//10
##
##print(sum)

#############################################################

##Armstrong number==153

##num=int(input("Enter a number"))
##temp=num
##digits=len(str(num))
##sum=0
##
##while temp>0:
##    ls=temp%10
##    sum=sum+ls**digits
##    temp//=10
##
##if sum==num:
##    print("Armstrong number")
##else:
##    print("Not a Armstrong number")

#######################################################

##star pattern
##num=5
##for i in range(1,6):
##    for j in range(1,i+1):
##        print("*",end=" ")
##
##    print()


##num=5
##for i in range(1,6):
##    for j in range(num-i):
##        print(" ",end=" ")
##    for k in range(i):
##        print("* ",end="  ")
##
##    print()

###################################################

##factorial
##num=int(input("Enter a number"))
##fact=1
##if num<1:
##    print("Factorial not defined for -ve numbers")
##else:
##    for i in range(1,num+1):
##        fact*=i
##
##print(fact)

##recursion method
##def factorial(num):
##    if num==0 or num==1:
##        return 1
##    return num*factorial(num - 1)
##
##num=int(input("Enter a number"))
##
##if num<0:
##    print("Factorial not defined for negative numbers")
##else:
##    print("Factorial=",factorial(num))


############################################################
#STRING
#palindrome
##str=input("Enter a string")
##rev=""
##for ch in str:
##    rev=ch+rev
##
##if rev==str:
##    print("palindrome")
##else:
##    print("not")


#count vowels and consonants
##str=input("Enter a String:  ")
##vowels,consonants=0,0
##for ch in str:
##    if ch in "aeiouAEIOU":
##        vowels+=1
##    else:
##        consonants+=1
##
##
##print(vowels,consonants)

##########################################################
##str1=input("Enter a string")
##str2=input("Enter a string 2")
##
##if sorted(str1)==sorted(str2):
##    print("Anagrams")
##else:
##    print("Not anagrams")


##str1=input("Enter a string: ").lower()
##str2=input("Enter a string2: ").lower()
##
##if sorted(str1)==sorted(str2):
##    print("Anagrams")
##else:
##    print("Not anagrams")

############################################################
# find largest ele
##nums=list(map(int,input("Enter numbers: ").split()))
##largest=nums[0]
##for num in nums:
##    if num>largest:
##        largest=num
##print("Largest =",largest)
    
############################################################        

##nums = list(map(int, input("Enter numbers: ").split()))
##largest = nums[0]
##for num in nums:
##    if num > largest:
##        largest = num
##print("Largest =", largest)

#################################################################
#second largest
##nums = list(map(int, input("Enter numbers: ").split()))
##nums = list(set(nums))
##nums.sort()
##
##if len(nums) < 2:
##    print("No second largest element")
##else:
##    print("second Largest=",nums[-2])



# sum of array
##nums= list(map(int, input("Enter elements: ").split()))
##total=0
##for num in nums:
##    total+=num
##
##print("Sum =",total)



#remove duplicate
##nums=list(map(int, input("Enter elements: ").split()))
##
##unique=[]
##for num in nums:
##    if num not in unique:
##        unique.append(num)
##print(unique)

##################################################################
# find frequency

##nums=list(map(int, input("Enter elements: ").split()))
##freq={}
##for num in nums:
##    freq[num] = freq.get(num,0)+1
##
##for key, value in freq.items():
##    print(key,"->",value)


####################################################################
#fibonacci series
##num=int(input("Enter the number of terms"))
##a,b=0,1
##
##for i in range(num):
##    print(a,end=" ")
##    a,b = b,a+b


#################################################################
#factorial
##num=int(input("Enter a number"))
##fact=1
##if num<1:
##    print("no factorial for negative number")
##else:  
##    for i in range(1,num+1):
##        fact*=i
##
##print(fact)

#######################################################
#swap w/o temp//////////////////////////////////////////////////////////////

##a = int(input("Enter first number: "))
##b = int(input("Enter second number: "))
##
##a, b = b, a
##
##print("After swapping:")
##print("a =", a)
##print("b =", b)

########################################################
#gcd-euclidian algo/////////////////////////////////////////////////////////
##a=int(input("Enter first number: "))
##b=int(input("Enter second number: "))
##
##while b!=0:
##    a,b = b,a%b
##
##print("GCD=",a)

######################################################
##lcm

##def gcd(a,b):
##    while b!=0:
##        a,b=b,a%b
##    return a
##
##print(gcd)
##
##a=int(input("Enter a number"))
##b=int(input("Enter second number"))
##lcm=(a*b)//gcd(a,b)
##print(lcm)

###########################################################
#missing number in array
##nums=list(map(int,input("Enter the nums: ").split()))
##n=len(nums)+1
##expected_sum=n*(n+1)//2
##actual_sum=sum(nums)
##
##missing=expected_sum - actual_sum
##print("missing number", missing)

##############################################################
#linear search
##nums=list(map(int, input("Enter numbers: ").split()))
##key=int(input("enter a key"))
##found=False
##
##for i in range(len(nums)):
##    if nums[i]==key:
##        print("key found at index",i)
##        found=True
##        break
##    
##if not found:
##    print("Key not presesnt")

##########################################################
#binary search
##def binary_search(nums,low,high,key):
##    if low>high:
##        return -1
##
##    mid=(low+high)//2
##
##    if nums[mid]== key:
##        return mid
##    elif nums[mid]<key:
##        return binary_search(nums,mid+1,high,key)
##    else:
##        return binary_search(nums,low,mid -1,key)
##
##nums=list(map(int,input("Enter sorted elements: ").split()))
##key=int(input("Enter element to search: "))
##
##result = binary_search(nums,0,len(nums)-1,key)
##
##if result != -1:
##    print("Element found at index", result)
##else:
##    print("Element not found")

############################################################
#bubble sort
##nums=list(map(int, input("Enter elements: ").split()))
##n=len(nums)
##
##for i in range(n):
##    for j in range(0,n-i-1):
##        if nums[j] > nums[j+1]:
##            nums[j],nums[j+1]=nums[j+1],nums[j]
##
##print("sorted array:" , nums)

############################################################
#Count even and odd numbers
##nums=list(map(int,input("Enter the numbers ").split()))
##even_sum=0
##odd_sum=0
##
##for i in nums:
##    if i%2==0:
##        even_sum+=i
##    else:
##        odd_sum+=i
##
##print("even_sum:", even_sum, "odd_sum: ",odd_sum)

###########################################################
#add two list
##arr1=list(map(int,input("Enter the elements").split()))
##arr2=list(map(int,input("Enter the elements").split()))
##merge=[]
##
##for i in arr1:
##    if i not in merge:
##        merge.append(i)
##
##for j in arr2:
##    if j not in merge:
##        merge.append(j)
##        
##merge.sort()
##
##print("Merge array: ", merge)


#############################################################
# move zeros to end
##nums=list(map(int,input("enter elements: ").split()))
##j=0
##for i in range(len(nums)):
##    if nums[i] != 0:
##        nums[j],nums[i] = nums[i],nums[j]
##        j+=1
##
##print("Result:",nums)

#################################################################
#two sum
nums=list(map(int,input("Enter elements: ").split()))
target=int(input("Enter target: "))
seen= set()

for num in nums:
    complement= target-num

    if complement in seen:
        print("pair: ", complement, num)
        break

    seen.add(num)













# practice
##def binary_search(nums,low,high,key):
##    if low> high:
##        return -1
##
##    mid=(low+high)//2
##
##    if nums[mid]==key:
##        return mid
##    elif nums[mid]<key:
##        return binary_search(nums,mid+1, high,key)
##    else:
##        return binary_search(nums, low,mid-1, key)
##
##nums=list(map(int, input("Enter sorted list: ").split()))
##key=int(input("enter element to search: "))
##
##result= binary_search(nums,0,len(nums)-1,key)
##
##if result != -1:
##    print("Element found at index",result)
##else:
##    print("Element not found")

# bubble sort
##nums=list(map(int, input("Enter the numbers:")))
##n=len(nums)
##
##for i in range(n):
##    for j in range(0,n-i-1):
##        if nums[j]> nums[j+1]:
##            nums[j], nums[j+1]=nums[j+1],nums[j]
##            
##
##

##a=int(input("Enter first number"))
##b=int(input("Enter second number"))
##
##a,b = b,a
##
##print("After swapping")
##print("a=",a)
##print("b=",b)

##############################################################

#fibbon
##num=int(input("Enter the numbers of terms"))
##a,b=0,1
##
##for i in range(num):
##    print(a,end=" ")
##    a,b = b, a+b
    
#########################################################

# lcm
##def gcd(a,b):
##    while b!=0:
##        a,b = b,a%b
##        return a
##
##a=int(input("Enter a number"))
##b=int(input("Enter second number"))
##lcm=(a*b)//gcd(a,b)
##
##print(lcm)

##################################################################

# missing nums
##nums=list(map(int,input("Enter the numbers: ").split()))
##n=len(nums)+1
##
##expected_sum=n*(n-1)//2
##actual_sum=sum(nums)
##
##missing=expected_sum - actual_sum
##
##print("missing number",missing)


################################################################












