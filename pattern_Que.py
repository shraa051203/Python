#####pattern programs###########
#wap to print given pattern
##*
##**
##***
##****
##*****
 
##num=5
##for i in range(1,num+1):
##    for j in range(i):
##        print("*", end=" ")
##    print()

##2 
##num=5
##for i in range(1,num+1):
##    for j in range(i):
##        print(i,end=" ")
##    print()

##num=5
##for i in range(1,num+1):
##    for j in range(1,i+1):
##        print(j,end=" ")
##    print()


##num=5
##for i in range(65,70):
##    for j in range(65, i+1):
##        print(chr(i),end=" ")
##    print()

##num=5
##for i in range(65,70):
##    for j in range(65, i+1):
##        print(chr(j),end=" ")
##    print()

##for lower case
##num=5
##for i in range(97,103):
##    for j in range(97, i+1):
##        print(chr(j),end=" ")
##    print()

##num=5
##for i in range(1,num+1):
##    for j in range(num-i):
##        print("-", end=" ")
##    for k in range(i):
##        print("*",end=" ")
##    print()


##num=5
##for i in range(1,num+1):
##    for j in range(num-i):
##        print("-", end="")
##    for k in range(i):
##        print("*",end=" ")
##    print()

##num=5
##for i in range(num,0,-1):
##    for s in range(num-i):
##        print("  ", end=" ")
##    for j in range(i):
##        print("* ", end=" ")
##    print()

###using single for loop####
##num=5
##for i in range(1,num+1):
##    print("*"*i)

##num=5
##for i in range(num,0,-1):
##    print("*"*i)

##num=5
##for i in range(1, num+1):
##    print("  "*(num-i)+"* "*i)

##num=5
##for i in range(num,0,-1):
##    print("  "*(num-i)+"* "*i)

##num=5
##for i in range(1,num):
##    print(" "*(num-i)+"* "*i)
##for i in range(num,0,-1):
##    print(" "*(num-i)+"* "*i)


##hw
##* * * * *
##*       *
##*       *
##*       * 
##* * * * *
rows=10
cols=10
for i in range(1, rows+1):
    if i in (1,rows):
        print("* "*cols)
    else:
        print("*"+"  "*(cols-2)+" *")





