##array

#####Two sums 
##def twosums(nums, target):
##    seen={}
##
##    for i in range(len(nums)):
##        needed = target - nums[i]
##
##        if needed in seen:
##            return [seen[needed],i]
##        seen[nums[i]]=i
##
##    return[]
##
##print(twosums([3,4,5,6,7,7,6,5],14))


####################two sums

##def twosums(nums, target):
##    seen={}
##
##    for i in range(len(nums)):
##        needed= target- nums[i]
##
##        if needed in seen:
##            return [seen[needed], i]
##        seen[nums[i]]=i
##
##    return[]
##
##print(twosums((7,8,9),5))


##################################################################
# move zeros to end

##def movezeros(nums):
##    j=0
##    for i in range(len(nums)):
##        if nums[i]!= 0:
##            nums[j], nums[i]= nums[i], nums[j]
##            j+=1
##    return nums
##
##print(movezeros([0,0,0,9,8,7,6]))



##########
##def movezeros(nums):
##    j=0
##    for i in range(len(nums)):
##        if nums[i]!=0:
##            nums[i], nums[j]= nums[j], nums[i]
##            j+=1
##    return nums
##
##print(movezeros([7,9,0,8,3,4,0,6]))

####################################################
# find missing nu
##def missingnumber(nums):
##    return sum(range(len(nums)+1)) - sum(nums)
##
##print(missingnumber([1,3,4,0]))


##def missingnumber(nums):
##    return sum(range(len(nums)+1)) - sum(nums)
##
##print(missingnumber([1,0,4,2]))
##

###############################################
# valid anagrams

##def isanagrams(s,t):
##    return sorted(s)== sorted(t)
##
##print(isanagrams("shraa", "aashr"))



##
##def isanagram(t,s):
##    return sorted(t)==sorted(s)
##print(isanagram("banana","nanaba"))

################################################

#reverse a string
##rev=""
##name= "shraddha"
##for i in range(len(name)):
##    rev=name[i]+rev
##
##print(rev)

#################################
##sum of n natural number

##num=10
##sum=0
##i=1
##while i<=num:
##    sum+=i
##    i+=1
##print(sum)

############################
##list=[22,56,90,87,77,67,89]
##i=0
##while i<=len(list):
##    if list[i]%2==0:
##        print(f'{list[i]} is Even')
##    else:
##        print(f'{list[i]} is odd')
##    i+=1

######################################

# print even numbers in single line
##i=0
##while i<=10:
##    print(i, end=" ")
##    i+=2

################################################
#palindrome
##num=12321
##rev=0
##i =num
##
##while i!=0:
##    last_digit= i%10
##    rev=rev*10+last_digit
##    i=i//10
##
##if num==rev:
##    print("palindrome")
##else:
##    print("Not palindrome")

##################################################

# display sum of numbers collecting start and end from the user
##start= int(input("Enter the start number: "))
##end= int(input("Enter the end number: "))
##sum=0
##while start <= end:
##    sum += start
##    start+=1

##print(sum)


##################################

#sum of list numbers
##lst=list(map(int,input().split()))
##sum=0
##for i in range(len(lst)):
##    sum+=lst[i]
##
##print(sum)

#######################################
















