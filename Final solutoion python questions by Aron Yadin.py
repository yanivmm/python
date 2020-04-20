
#####################################################################

#Author : Yaniv Maimon
#year   : 2019
#job    : final questions file of introduction to computer science 
    
#####################################################################


#1
x=input("enter a num:")
t,z,summ = 0,0,0
for i in x:
    if int(i)>t:
        t = int(i)
    if int(i)<z:
        z=int(i)
    summ+=int(i)
print("the sum is:",summ ,"\n","the min is:",z,'\n',"the max is",t)


#2
x,y = input("enter a num please:"),input("enter a second num please:")
a=''
while len(x)!=len(y):
    print("the tow numbers must have the same length")
    x,y = input("enter a num please:"),input("enter a second num please:") 
for i in range(len(x)):
     a+=(str(y)[i]) if int(str(x)[i])>=int(str(y)[i]) else (str(x)[i])
a


#3
x = 346783445 #input("enter a second num please:")
a='' 
t = len(str(x)) if len(str(x))%2==0 else len(str(x))-1
for i in range(0,t,2):
    a+=(str(x)[i+1]) if str(x)[i]>=str(x)[i+1] else (str(x)[i])
print(a) if len(str(x))%2==0 else print(a+str(x)[-1])


#4

x = input("enter a num please:")
a= 0 
for i in x:
    a+=i
    print(a)


#5
x = input("enter a second num please:")
a,x = 1,str(x) 
for i in x:
    i=int(i)
    if i!=0:
        a*=i
    print(a)

#6
import math
x = 346783407804565 #input("enter a second num please:")
a,x = 1,str(x)
t = math.floor(len(str(x))/2) 
if len(x)%2 == 0:
    [print(int(x[i])+int(x[-i-1])) for i in range(t)]
else:
    [print(int(x[i])+int(x[-i-1])) for i in range(t)]
    print(2*int(x[t+1]))



#7
i=0
x = 346
while x!=1:
    if x%2==0:
        x=int(x/2)
        print("(",i,")   ",x)
    else:
        x=x*3+1
        print("(",i,")   ",x)
        i+=1


#10
from math import *
p,d=0,0
#x = 100 int(input("enter num of iterations: "))
for x in {100,5000,1000000}:  
    for i in range(1,x,4):
        d+=(1/i)
    for i in range(3,x,4):
        p+=(1/i)
    PI = 4*(d-p)
    print("For",x,"the pi is",round(PI,10),"and the error is: " ,round(abs(PI-pi),10))

#11
a,x='',input("enter string: ")
for i in x:
    if i in 'abc':
        a+='2'
    elif i in 'def':
        a+='3'
    elif i in 'ghi':
        a+='4'
    elif i in 'jkl':
        a+='5'
    elif i in 'mno':
        a+='6'
    elif i in 'pqrs':
        a+='7'
    elif i in 'tuv':
        a+='8'
    elif i in 'wxyz':
        a+='9'
    elif i == '1':
        a+='1'
    elif i == '0':
        a+='0'
print(a)


#12
year,a,b=0,20*10**6,10*10**6
while a>b:
    a*=1.02
    b*=1.03
    year+=1  
print("after ",year," years: country A will have ",round(a),
      " habbitants, and country B will have ",round(b)," habitants.")


#13
d,b,c,a="","","","I1 1w1i1l2 1f1e2l1 1g1o2d1 1s1o2n1!1"
for i in range(len(a)):
    if i%2==0:
        b+=a[i]
    else:
        c+=a[i]
for i in range(len(b)):
    d+=b[i]*int(c[i])
print(d)


#14 
d,b,c,a="","","","abcdefghi"
for i in range(len(a)):
    if i%2==0:
        b+=a[i]
    else:
        c+=a[i]
c=c[::-1]
print("The original string is",a,"\n The new one is ",b+c)


    
#15
a=int(input())
for i in range(a):
    string=(2+i*4)*"*"
    new = string.center(48, ' ')
    print(new)
    print(new)



#16
letters,text,c = "rtf",input(),0
for i in letters:
    for x in text:
        if i == x:
            c+=1
    print("The times the letter ",i," is in the text is ",c)
    c=0
    
#17
l=''
x=int(input())
for i,letter in enumerate(str(x)):
    i+=1
    a = i*int(letter)
    if a>10:
        a = a%10
    l+=str(a)
l

#18
x=str(123456)
print(x)
for i in range(len(x)):
    x=x[1:]
    x=x[::-1]
    print(x)
    
#19
cnt=0
x="[]][][][][][][[]][]["
for i in x:
    if i=="[":
        cnt+=1
    elif i=="]":
        cnt-=1
    if cnt<0:
        break
print(cnt==0)

#20
heads = int(input("enter amount of heads "))
legs = int(input("enter amount of legs "))
print("the amount of rabbits is: ",int(2*heads - 0.5*legs))
print("the amount of chickens is: ",int(heads - (2*heads - 0.5*legs)))

#21
x= int(input())
print(any([x%9==0, x%12==0, x%20==0]))


#22
x,sum = input("enter number: ")[::-1],0
for i,e in enumerate(x):
    sum+=int(e)*(i+1)
print(sum%11==0)


#23
a=""
x= "mississippi"+" "  # input()
for i in range(len(x)-1):
    if x[i]!=x[i+1]:
        a+=x[i]
print(a)

#24 A
x,sum=input("enter a number: "),0
if len(x)%2==0:
    for i in range(0,len(x),2):
        sum+=(int(x[i])*int(x[i+1]))
else:
    for i in range(0,len(x)-1,2):
        sum+=(int(x[i])*int(x[i+1]))
    sum+=int(x[-1])
print(sum)
    
#24 פתרון נוסף

summ=0
x=input('enter a number: ') + '1'
for i in range(0,len(x)-1,2):
    summ += int(x[i])*int(x[i+1])
print(summ)

#25
a=""
x="99999"
y="876"
for i in range(min(len(x),len(y))):
    a+=str(int(x[i])*int(y[i])).zfill(2)
print(a)

#26,27 נפתר

#28

a="hjiol,mkl"
print(a[::-2])

#29
import math
sterling,atz,x,y = 0,1,1,10
for i in range(x,y):
    for j in range(i,0,-1):
        atz*=j
    sterling = math.sqrt(2*math.pi*i)*(i/math.e)**i
    print(f'{f"{i}":<7}{f"{sterling}":<25}{f"{atz}"}')
    atz=1

#30 unfinished
l=[]
x= [[4,5,2,54],[12,21,-54,3,2,4,76,5],[4,3,2,1]]            # list(input("enter list: ")
for i in x:
    l.append(sum(i))
print(sorted(l)[0])


#31
x = "The five boxing wizards jump quickly"    #input("enter:")
l=[]
for i in x.lower():
    if ord(i) not in l and ord(i)>96 and ord(i)<123:
        l.append(ord(i))
print(len(l)==26)

#32
a,x='',int(input("enter num: "))
for i in range(1,x+1):
    for j in range(1,i+1):
        a+=str(i*j)+" "
    print(a)
    a=""


#33
l1,l2=[],[]    
mone,mchn=124,256
for i in range(1,min(mchn//2,mone//2)):
    if mone%i==0:
        l1.append(i)
    if mchn%i==0:
        l2.append(i)
        
intersection = [value for value in l1 if value in l2]
val = intersection[-1]  #the biggest value in the intersection. It is also the both nums highest diveider
print(int(mone/val),"/",int(mchn/val))


#34
x=1234567890
st = "one two three four five six seven eight nine zero".split()
for i in str(x):
    print(st[int(i)-1], end='/')


#35
import math

def atz(x):  
    atzr=1 
    for i in range(x,1,-1):
        atzr*=i
    return atzr

E=0
y=int(input())
for i in range(y):
    E += 1/atz(i)
    print((E-math.e)*(-1))


#36
l=[]
x=12345654321
for i in str(x):
    for j in str(x):
        if int(i)+int(j) == 7 and [i,j] not in l and [j,i] not in l:
            l.append([i,j])
            print(i,j)


#37
l,b,x=[],True,int(input("enter number: "))
for i in str(x):
    if i not in l:
        l.append(i)
    else:
        b=False
        break
print(b)


#38

def uniqe(x):
    b=True
    for j in str(x):
        if str(x).count(j)!=1:
            b=False
    return b

sum=0
a,b=int(input()),int(input())
for i in range(a,b):
    if uniqe(i):
        sum+=i
print(sum)

#39

b = input("student? write true or false: ")
x= int(input())
if b.lower()=="true":
    a=0.8 if x>250 else 0.85
else:
    a=0.85 if x>400 else 0.95
print(a*x)
print(b)


#40 a damn long one
def yes(x):
    x=str(x)
    b=False
    if int(x[0])%2==1 and int(x[-1])%2==1:
        b=True
    return b


sum = 0
i = 33  #this value is the first one that answers the question
a=''
n= int(input("enter the number of nums you wish to present: "))
while sum<n:
    if yes(i**2):
        a+= str(i**2) +' '
        sum+=1
    b=a.split()    # b= items added to a
    if len(b) == 5 or sum==n :  #sum%5==0: (less optional)
        #the condition above sais 'when you get to 5 items or you have no other numbers to add- than print'
        for d in range(len(b)):
            print(f'{f"{b[d]}":<7}',end = "")  #printing font of every number added with permanent space of 7 chars 
        print()               #after 5 numbers printed, skip line.        
        a=''          #reboot 'a' after printing it
    i+=1        

#41
def T(x):
    print(x**2+x+1)

#42    
x='fghjkjhghbnjk' #input()
leng = min(len(x),11)
for i in range(0,leng,2):
    print(x[:(i+1)].center(leng*2, ' '))    
for i in range(leng-2,0,-2):
    print(x[:i].center(leng*2, ' '))    

    
#43
def bina(x):
    sum=0
    for i in x:
        sum+=int('0b'+str(i),2)
    print(bin(sum)[2:])
    
bina([1010,10111,101111])
 

#44
a=''
x=input().strip()
for c,i in enumerate(x):
    if x[c]==' ' and x[c+1]==' ':
        continue
    else:
        a+=i
a


#45
for i in range(100,1000):
    d=0
    for j in str(i):
        d+= int(j)**3
    if d==i:
        print(i,end= ' ')


#46 nice code long running time
n=int(input())
for i in range(10**(n-1),10**n):
    d=0
    for j in str(i):
        d+= int(j)**n
    if d==i:
        print(i,end= ' ')
        
#47 hex decimal
    
    
#48
l=[]
x=["This","is","a","small","example"]
[l.append(len(i)) for i in x]
n = max(l)

a='*'
print("*"*(n+4))
for i in x:
    print(f'{f"*":<2}{f"{i}":<{n+1}}{f"*"}')
print("*"*(n+4))



#49
sum=0
x=int(input())
while len(str(x))!=1:
    for i in str(x):
        sum+=int(i)
    x=sum
    sum=0
print(int(x))


#50
x=76812947348873164
sum=0
for i in str(x):
    sum+=int(i)
d =sum/len(str(x))

for i in str(x):
    i=int(i)
    if i==d:
        print('A',end='')
    elif i>d:
        print('H',end='')
    else:
        print('L',end='')


############## ex' 11 YVC freshmen ###########


#1
def A(n):
    if n==1:
        return 20
    else:
        return 3+10/A(n-1)

for i in range(5):
    print(i,A(i))

def PT(n,k):
    if n==k or k==0:
        return 1
    else:
        print(n,k)
        return PT(n-1,k)+PT(n-1,k-1)
    


#3 ex 11
x=7682887364
d = list(str(x))
maxi = str(max(d))
mini = str(min(d))
for i in range(d.count(mini)):
    d.remove(mini)
for i in range(d.count(maxi)):
    d.remove(maxi)

d

#4 ex 11
l = []
x = input("enter num of nums seperated with space ' ':\n ").split()
a = x.copy()
for i in range(len(x)):
    l.append(x[i])
    l.append(a[i])
l


#5 ex 11

names="amos yoav habakuk noga shlomi"
ages =[87,42, 96,205,214]
names = names.split()
 #ages=sorted(ages,reverse = True)
oldestIndex = ages.index(max(ages))
names[oldestIndex]


#6 ex 11
l=[]
a=input("enter string body: \n")
while a!='':
    l.append(a)
    a=input("enter string body: \n")
r=[]
for i in l:
    for j in i.split():
        if j not in r:
            r.append(j)
print(sorted(r))












