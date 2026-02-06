RECURSION
-It is process of calling the function by itself until given
condition terminates
-In python function can call itself 1020 times(Maximum recursion
                                               depth)
- Whenever there is a task of reverse traceback or to avoid nested
loop implementation we can use recursion


# nums from 1 to 10 using recursion
##def numbers(i=1):
##    if i<=10:
##        print(i)
##        numbers(i=i+1)
##numbers()

# even numbers from 100 to 1
##def even_no(i=100):
##    if i>=1:
##        print(i)
##        even_no(i=i-2)
##
##even_no()

# acces character of given string using rec
##name="shraddha"
##def print_char(st,i=0):
##    if i<len(st):
##        print(st[i])
##        print_char(st,i=i+1)
##print_char(name)

##name="shraddha"
##def print_char(name,i=0):
##    if i<len(name):
##        print(name[i])
##        print_char(name,i=i+1)
##print_char(name)

#
##list=[10,20,30,40,50,60]
##def print_num(lst,i=0):
##    if i < len(lst):
##        print(lst[i])
##        print_num(lst,i=i+1)
##print_num(list)

##lst=["apple","tcs","microsoft","ibm"]
##def names(v,i=0):
##    if i<len(v):
##        print(v[i])
##        names(v,i=i+1)
##names(lst)

#extract all vowels from the list
##name="allu arjun"
##def extract_vow(st,v='',i=0):
##    if i<len(st):
##        if st[i] in "aeiouAEIOU":
##            v+=st[i]
##        return extract_vow(st,v,i=i+1)
##    return v
##print(extract_vow(name))

# extract integers from list
##data=[10,'apple',20,True,4.5,40]
##def numbers(lst,v=[],i=0):
##    if i < len(lst):
##        if type(lst[i])==int:
##            v.append(lst[i])
##        return numbers(lst,v,i=i+1)
##    return v
##print(numbers(data))
    

#extract all the vowels present inside string list
##names=["apple","google","tcs","microsoft","ibm"]
##def vowels(lst,v=[],i=0):
##    if i<len(lst):
##        for ch in lst[i]:
##            if ch in "aeiouAEIOU":
##                v.append(ch)
##        return vowels(lst,v,i=i+1)
##    return v
##print(vowels(names))

##input=[(1,2,3,4,5),
##        (6,7,8,9,10),
##        (20,30,40,50)]
### output=[1,2,3,4,5,6,7,8,9,10,20,30,40,50]
##
##def output(lst,out=[],i=0):
##    if i < len(lst):
##        for num in lst[i]:
##            out.append(num)
##        return output(lst,out,i=i+1)
##    return out
##print(output(input))

# factorial
def fact(num):
    if num in (1,0):
        return 1
    return num*fact(num-1)

print(fact(3))




