###################nested loop
##lst_names=["apple","google","tcs"]
##for names in lst_names:
##    for char in names:
##        print(char)

#wap
##input=[12,"hai","hello", 89,8,9,"python"]
##output=["hai":2,"hello":2,"python":1]
##output={}
##for i in input:
##    if type(i)==str:
##        count=0
##        for ch in i:
##            if ch in "aeiouAEIOU":
##                count+=1
##            output[i]=count
##print(output)


##output={}
##for i in input:
##    if type(i)==str:
##        count=0
##        for ch in i:
##            if ch in "aeiouAEIOU":
##                count+=1
##            output[i]=count
##print(output)

#wap to get foll output
##input=[12,"hai",89,"program",6.7,"python"]
####output=[12,"iah",89,"margorp",6.7,"nohtyp"]
##
##output=[]
##for i in input:
##    if type(i)==str:
##        rev=""
##        for ch in i:
##            rev=ch+rev
##        output.append(rev)
##    else:
##        output.append(i)
##print(output)



#####wap
##st="python is very easy"
####output={"python":6,"is":2,"very":4,"easy":4}
##output={}
##for i in st.split():
##    count=0
##    for ch in i:
##        count+=1
##    output[i]=count
##    
##print(output)  



#####################PATTERN QUESTION
##num =5
##for i in range(1,6):
##    for j in range(i):
##        print("*",end=" ")
##    print()

##num=5
##for i in range(1,6):
##    for j in range(1,i+1):
##        print(j,end=" ")
##    print()

##num=5
##for i in range(1,6):
##    for j in range(i):
##        print(i,end=" ")
##    print()


##for i in range(65,70):
##    for j in range(65,i+1):
##        print(chr(i),end=" ")
##    print()

##for i in range(65,70):
##    for j in range(65,i+1):
##        print(chr(j),end=" ")
##    print()

##for i in range(97,102):
##    for j in range(97,i+1):
##        print(chr(i),end=" ")
##    print()
##
##for i in range(97,102):
##    for j in range(97,i+1):
##        print(chr(j),end=" ")
##    print()


##
##num=5
##for i in range(1,num+1):
##    for j in range(num-i):
##        print("  ",end="")
##    for k in range(i):
##        print("* ",end="  ")
##    print()
##
##
##num=5
##for i in range(1,num+1):
##    for j in range(num-i):
##        print("--",end=" ")
##    for k in range(i):
##        print("* ",end=" ")
##    print()

##num=5
##for i in range(1,num+1):
##    for j in range(num-i):
##        print("",end="")
##    for k in range(i):
##        print("* ",end="")
##    print()

##num=5
##for i in range(num,0,-1):
##    for s in range(num-i):
##        print(" ",end=" ")
##    for j in range(i):
##        print("*",end=" ")
##    print()

#######short using single loop
##num=5
##for i in range(1,num+1):
##    print("*"*i)

##num=5
##for i in range(num,0,-1):
##    print("*"*i)

##num=5
##for i in range(1,num+1):
##    print(" "*(num-i)+"* "*i)
##for i in range(1,num+1):
##    print(" "*i+"* "*(num-i))

##num=5
##for i in range(num,0,-1):
##    print(" "*(num-i)+"*"*i)


##rows=10
##cols=10
##for i in range(1,rows+1):
##    if i in (1,rows):
##        print("* "*cols)
##    else:
##        print("* "+"  "*(cols-2)+"* ")

########################COMPREHENSION
##var_name=[expression for item in iterable]
##var_name=[expression for item in iterable if condition]
##var_name=[TSB if condition else FSB for item in iterable]
##var_name=[expression for item in iterable for value in item]

#list of char in given string
##str='hello'
##print([ch for ch in str])

##numbers=[1,2,3,4,5]
##print([num**2 for num in numbers])

##build first and last name from full name

##names=["james bond","virat kohli","priyanka chopra","vijay raj"]
##print([name.split()[0] for name in names])
##
##print([name.split()[1] for name in names])

#list of even numbers from 1 to 20
##print([num for num in range(1,21) if num%2==0])

#list of palindromes from given list
##names=["steve","eve","john","Anna","Bob"]
##print([name for name in names if name.upper()==name[::-1].upper()])


#names less than six char
##names=["apple","google","tcs","microsoft","flipkart","instagram"]
##print([name for name in names if len(name)>6])

#filter languages start with p
##languages=["python","java","perl","php","js","c++","ruby"]
##print([lang for lang in languages if lang.startswith("p")])


#build list with only even lengthstr
##names=["apple","google","tcs","microsoft","flipkart","instagram"]
##print([name for name in names if len(name)%2==0])
##

#reverse the item of list if it is odd length else keep as it is
##names=["apple","google","tcs","microsoft","flipkart","instagram"]
##print([name[::-1] if len(name)%2!=0 else name for name in names])

#add items of two list
##a=[1,2,3,4]
##b=[5,6,7,8]
##
##sum=[]
##for v1,v2 in zip(a,b):
##    sum.append(v1+v2)
##print(sum)
##
##print([v1+v2 for v1,v2 in zip(a,b)])

##a=[1,2,3,4,5]
##b=[6,7,8,9,10]
##c=[11,12,13,14,15]
##sum=[]
##
##for i1,i2,i3 in zip(a,b,c):
##    sum.append(i1+i2+i3)
##
##print(sum)

##for v in enumerate('apple'):
##    print(v)
##
##list=[33,44,55,66,77,88,99]
##for i,value in enumerate(list):
##    print(i,value)

####################SET COMPREHENSION
##var_name={expression for item in iterable}
##var_name={expression for item in iterable if condition}
##var_name={TSB if condition else FSB for item in iterable}
##var_name={expression for item in iterable for value in item}


##names=["apple","tcs","ibm","microsoft","google","flipkart","gmail","yahoo"]
##name_len=set()
##print({(name,len(name)) for name in names})


###############DICT COMPRESSION
##{key: value for value in collection}
##{key:value for value in collection if condition}
##{key: value if condition else key:value for value in collection}
##{key:value for value in collection for element in value}

#build a dict and length pair
##sentence="i am shraddha chatrulal kharatmal"
##print({word:len(word) for word in sentence.split()})

#flipping key and value
##d={"a":1,"b":2,"c":3}
##print({d[key]:key for key in d})

#counting number of char in each word
##sentence="hello world welcome to python hi yoo i am learning python"
##print({ch:sentence.count(ch) for ch in sentence if ch!=' '})


#dict of word and its count pair
##sentence="hello world welcome to python hi yoo i am learning python"

##print({word:sentence.split().count(word) for word in sentence.split()})

#convert height from meter to feet
##building={"om":828,"shanghai":678,"clock_tower":788}
##print({build:building[build]*3.28 for build in building})


#city and population pairs
##cities=["tokyo","delhi","shanghai","new_york"]
##population=['564,78,759','67,78,900','56,78,900','34,56,766']
##
##print({v1:v2 for v1,v2 in zip(cities,population)})


###reverse code and country 
##dial_codes=[(86,"china"),(91,"india"),(1,"usa"),(55,"Brazil")]
##
##print({country:code for code,country in dial_codes})

#build dict whose price is more than 2000
prices={"mobile":7000,"ac":8000,"mixer":1500,"remote":800,"laptop":56000}

print({item:prices[item] for item in prices if prices[item]>2000})






