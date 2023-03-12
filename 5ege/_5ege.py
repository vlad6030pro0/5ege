'''
for i in range(1,1000):
    b = int(bin(i))
    k=str(b%2)+str(b//2%2)
    a = int(bin(i)+k,2)
    if(a>74):
        print(i)
        break
'''
'''
def schet(i):
    a = 0
    a+=int(i[:1])
    i=i[1:]
    a+=int(i[:1])
    return a

for i in range(1000,10000):
    p = i
    a,b,c = 0,0,0
    abc = [a,b,c]
    for n in range(3):
        abc[n]+=schet(str(i))
        i=str(i)[1:]
    abc.remove(min(abc))
    l = str(abc[0])+str(abc[1])
    if l=="1418":
        print(p)
        break
'''
'''
def schet(a):
    b = 0
    while a:
        b+=a%2
        a//=2
    return b
for i in range(1,1000):
    r = bin(i)[2:]+str(schet(int(bin(i)[2:]))%2)
    r = str(r)+str(schet(int(r))%2)
    if int(r,2)>154:
        print(int(r,2))
        print(i)
        break
    '''
'''
def schet(i):
    a = 0
    a += int(i[:1])
    i = i[1:]
    a += int(i[:1])
    return a

ans = []
for i in range(1000,10000):
    p = i
    a = 0
    b = 0
    c = 0
    abc = [a,b,c]
    i = str(i)
    for n in range(3):
        abc[n] = schet(i)
        i = str(i)[1:]
    abc.remove(min(abc))
    l = str(min(abc))+str(max(abc))
    if l == "613":
        ans.append(p)
print(max(ans))
'''
'''
for i in range(1,1000):

    r = bin(i)[2:]
    if int(r)%2==0:
        r = '1'+r+'0'
    else:
        r = '11'+r+'11'
    if (int(r,2)>52):
        print(i)
        break
'''
'''
def proverka(i):
    a = 0
    while i:
        if i%10%2==1:
            a+=1
        i//=10
    if a==4:
        return True
    return False
def s(i):
    i = str(i)
    b=0
    c=0
    a = ''
    b+=int(i[:1])
    i=i[1:]
    b+=int(i[:1])
    i=i[1:]
    c+=int(i[:1])
    i=i[1:]
    c+=int(i[:1])
    a += str(min(b,c))+str(max(b,c))
    return a

c=0
for i in range(1000,10000):
    if proverka(i):
        if (s(i)=="616"):
            c+=1
print(c)
'''
'''
def s(i):
    i = str(i)
    b=0
    c=0
    a = ''
    b+=int(i[:1])
    i=i[1:]
    b+=int(i[:1])
    c+=int(i[:1])
    i=i[1:]
    c+=int(i[:1])
    a += str(max(b,c))+str(min(b,c))
    return a
for i in range(100,1000):
    if(s(i)=="157"):
        print(i)
        break
'''
'''
def sumch(r):
    a = 0
    r = int(r)
    while r:
        a+=r%2
        r//=2
    return a

for i in range(1,1000):
    r = bin(i)[2:]
    r = r+str(sumch(r)%2)
    r = r+str(sumch(r)%2)
    if  int(r,2)<90:
        print(int(r,2))
'''
'''
def perevod(i):
    k=''
    while i :
        k=str(i%3)+k
        i//=3
    return k
for i in range(1,1000):
    r = perevod(i)
    r+=str(i%3)
    print(int(r,3))
'''
'''
def s(i):
    i = str(i)
    b=0
    c=0
    a = ''
    b+=int(i[:1])
    i=i[1:]
    b+=int(i[:1])
    c+=int(i[:1])
    i=i[1:]
    c+=int(i[:1])
    a += str(min(b,c))+str(max(b,c))
    return a
for i in range(100,1000):
    if(s(i)=="1115"):
        print(i)
        break
'''

        
        

    


    















