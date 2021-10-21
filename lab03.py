#Lab 03
#Nealson Setiawan
def multiply(x,y):
    if y != 0:
        if (y-1 == 0):
            return x 
        else:
            return x+multiply(x,y-1)

    else:
        return 0

def collectOddValues(listOfInt):
    n = []
    if(listOfInt != []):
        if(listOfInt[0]%2 == 1):
            n.append(listOfInt[0])
        
        return n + collectOddValues(listOfInt[1:])
    else:
        return []

def countInts(listOfInt, num):
    n = 0
    if(listOfInt != []):
        if isinstance(listOfInt[0],float):
            n = 0
            
        elif isinstance(listOfInt[0],int):
            if listOfInt[0] == num:
                n = 1

        else:
            n = 0
        return n + countInts(listOfInt[1:],num)

    else:
        return 0

def reverseString(s):
    if(s != ""):
        c = s[len(s)-1]
        return c + reverseString(s[0:len(s)-1])
    else:
        return ""

def removeSubString(s,sub):
    z = ""
    k = ""
    if(s != ""):
        c = s[0:len(sub)]
        if c == sub:
            z = s[len(sub):len(s)]
        else:
            k = s[0]
            z = s[1:]
        
        return k + removeSubString(z,sub)
    else:
        return ""

'''def collectOddValuesOld(listOfInt):
    x = 0
    for i in range(len(listOfInt)):
        if(listOfInt[i] % 2 != 1):
            if i == 0:
                x = -1
            else:
                x = i
            break
    
    if (x != 0):
        if i == 0:
            listOfInt.pop(0)
        else:
            listOfInt.pop(i)
            
        return (collectOddValues(listOfInt))
    else:
        return listOfInt

def countIntsOld(listOfInt, num):
    x = 0
    for i in range(len(listOfInt)):
        if(listOfInt[i] != num):
            if i == 0:
                x = -1
            else:
                x = i
            break
    
    if (x != 0):
        if i == 0:
            listOfInt.pop(0)
        else:
            listOfInt.pop(i)  
        return countInts(listOfInt, num)
    else:
        return len(listOfInt)
'''
