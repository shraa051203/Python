###print devices
##num=int(input("enter the number:"))
##for i in range(1,num+1):
##    if num%i==0:
##        print(i)
##
##
####sum of devices of given number excluding that number
##num=int(input("Enter the number:"))
##sum=0
##for i in range(1,num):
##    if num%i==0:
##        sum+=i
##
##print(sum)
##
##
####perfect number
##num=int(input("Enter the number:"))
##sum=0
##for i in range(1,num):
##    if num%i==0:
##        sum+=i
##
##if sum==num:
##    print("It is a perfect number")
##else:
##    print("It is not a perfect number")

##sum of all int + inside list
##lst=[10,"apple", 20,8.9,True,70]
##sum=0
##for i in lst:
##    if type(i)==int:
##        sum+=i
##
##print(sum)

######################################################
###string reverse
##st="shraddha"
##rev=''
##for ch in st:
##    rev=ch+rev
##
##print(rev)
##


#####################################################
#char along with there index number
##st= "shraa"
##char_index={}
##for index in range(len(st)):
##    char_index[index]=st[index]
##print(char_index)

#################################################
#string with its index
##lst=["shraa", "soniya", "aura","dhristi"]
##word_length={}
##for item in lst:
##    word_length[item]=len(item)
##
##print(word_length)
##    
##############################################
##prime number
##num=int(input("Enter the numver:"))
##for i in range(2,num):
##    count=0
##    if num%i==0:
##        count+=1
##
##if count>=1:
##    print("Not a prime number")
##else:
##    print("Prime number")

#############################
#if string return rev else save as it is
##lst=[20 ,True, 56, "shraa", 99.87, "Dhrishti"]
##output=[]
##for item in lst:
##    if type(item)==str:
##        rev=''
##        for char in item:
##            rev=char+rev
##        output.append(rev)
##    else:
##        output.append(item)
##
##print(output)
        
#######################################################
##st="Python is very easy"
##word_len={}
##for word in st.split():
##    count=0
##    for char in word:
##        count+=1
##    word_len[word]=count
##print(word_len)

















