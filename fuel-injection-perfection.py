d = {}
d['0'] = 0
d['1'] = 0
d['2'] = 1
d['3'] = 2
d['4'] = 2
d['5'] = 3
d['6'] = 3
d['7'] = 4
d['8'] = 3
d['9'] = 4

def divideByTwo(n):
    l = []
    num = 0
    for i in range(len(n)):
        num = num * 10 + int(n[i])
        q = num/2
        num = num%2
        if (q==0 and len(l)==0):
            continue
        l.append(str(q))
    if (len(l)==0):
        result = '0'
    else :
        result = ''.join(l)
    
    return result
    
def addOne(n):
    result = ''
    i = len(n) - 1

    while(n[i]=='9' and i >= 0):
        i = i  - 1
    result = '0' * (len(n) - i -1)
    
    if (i==-1):
        return '1' + result
    
    result = str(int(n[i]) + 1) + result
    i = i - 1
    
    if (i>=0):
        result = n[0:i+1] + result
        
    return result
    
def removeOne(n):
    result = ''
    i = len(n) - 1

    while(n[i]=='0' and i >= 0):
        i = i  - 1
        
    result = '9' * (len(n) - i -1)
    
    if (i==-1):
        return 'INVALID'
    
    result = str(int(n[i]) - 1) + result
    i = i - 1
    
    if (i>=0):
        result = n[0:i+1] + result
        
    return result
    
def isEven(n):
    return int(n[len(n)-1])%2==0


def getMinSteps(n):
    n = removeLeadingZeros(n)
    #print(n)
    if d.has_key(n):
        #print("FOUND")
        return d[n]
    else:
        if (isEven(n)):
            res = 1 + getMinSteps(divideByTwo(n))
        else:
            if (len(n)<3):
                check = (int(n)%4)==3
            else:
                temp = n[len(n)-2] + n[len(n) -1]
                check = (int(temp)%4)==3    
            if (check):
                res = 1 + getMinSteps(addOne(n))
            else:
                res = 1 + getMinSteps(removeOne(n))
                
        d[n] = res
        return res
                
        
    
     
def removeLeadingZeros(n):
    i = 0
    while (n[i]=='0' ):
        i = i+1
        if (i ==len(n)):
            break
        
    
    if (i==len(n)):
        return '0'
    else:
        return n[i:len(n)]
        
def getMinStepsIter(n):
    n = removeLeadingZeros(n)
    #print(n)
    if d.has_key(n):
        #print("FOUND")
        return d[n]
        
    steps = 0
    while (len(n)>1):
        if (isEven(n)):
            n = divideByTwo(n)
        else:
            if (len(n)<3):
                check = (int(n)%4)==3
            else:
                temp = n[len(n)-2] + n[len(n) -1]
                check = (int(temp)%4)==3 
            if (check):
                n = addOne(n)
            else:
                n = removeOne(n)
        steps = steps +1
    return steps + d[n]   

def solution(n):
    n = removeLeadingZeros(n)
    return getMinStepsIter(n)