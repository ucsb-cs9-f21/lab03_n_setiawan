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


def countInts(listOfInt, num):
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

assert countInts([1,2,3,4,3,2,1], 2) == 2
assert collectOddValues([0,1,2,3,4,5]) == [1,3,5]