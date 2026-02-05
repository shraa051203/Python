###########################################SET COMP


##def-it is a way to built set from sequences or any other iterable type by filtering and transforming items
##
##general syntax:
##var_name={expression for item in iterable}
##var_name={expression for item in iterable if condition}
##var_name={TSB if condition else FSB for item in iterable}
##var_name={expression for item in iterable for value in item}


# to avoid duplicated values


#Q1 WAP to get set of tuples with name and length
##names=['apple', 'google', 'yahoo', 'gmail', 'apple','google','flipkart', 'apple', 'google']
##names_len=set()
##for name in names:
##    names_len.add((name,len(name)))
##print(names_len)
##################################
##print({(name.len(name)) for name in names})


#######################################DICT COMP##############################

##it is phenomenon of creating new output dictionary by reducing the number of instruction
## taken to do the required operation
##syntax: {key:value for value in collection}
##        {key:value for value in collection if condition}
##        {kay:value if cond else k:v for value in collection}
##        {key:value for value in collection for element in value}


#Q1 build a dict of word and length pair
##sentence ='This is a bunch of words'
##word_len={}
##for word in sentence.split():
##    word_len[word]=len(word)
##print(word_len)
##
##print({word:len(word) for word in sentence.split()})


#Q2 flipping key and values of dict using dict compression
##d={'a':1, 'b': 2,'c':3}
##flip_d={}
##for k in d:
##    flip_d[d[k]]=k
##print(flip_d)
##
##print({d[k]:k for k in d})
##
##print({value:key for key, value in d.items()})


##Q3 counting the number of each character in a string
sentence=" hello world welcome to python hello hi world welcome to python "
##
##char_count={}
##for ch in sentence:
##    if ch in char_count:
##        char_count[ch] +=1
##    else:
##        char_count[ch]=1
##print(char_count)
##print({ch:sentence.count(ch) for ch in sentence if ch!=" "})


#4.creat a dictionary of word and its count pair from given string.

##sentence = "hello world welcome to python hello hi world welcome to python"

##word_dict={}
##for word in sentence.split():
##    if word in word_dict:
##        word_dict[word]+=1
##    else:
##        word_dict[word]=1
##print(word_dict)

print({word:sentence.split().count(word) for word in sentence.split()})


#5. Dictionary of Buildings and it height pairs by converting the height from
##meter to feet
##buildings = {
##'burj khalifa': 828,
##'Shanghai_Tower': 632,
##'Abraj_Al_Bait_Clock Tower': 601,
##'Ping_An_Finance_Centre_Shenzhen': 599,
##'Lotte World Tower': 554.5,
##'World Trade Center': 541.3}
####3.284
##build={}
##for k in buildings:
##    build[k]=3.284*k[build]
##print(build)




