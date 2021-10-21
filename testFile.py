from lab03 import countInts,removeSubString,collectOddValues,reverseString,multiply

'''
from lab03 import removeSubString
from lab03 import collectOddValues
from lab03 import reverseString
from lab03 import multiply
'''

assert multiply(5,4) == 20 #Professor's Example
assert multiply(1,2) == 2
assert multiply(0,0) == 0
assert multiply(12,0) == 0
assert multiply(20,3) == 60

assert collectOddValues([0,1,2,3,4,5]) == [1,3,5] #Professor's Example
assert collectOddValues([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9]
assert collectOddValues([0,1,2,3,3,3,3,6,13]) == [1,3,3,3,3,13]
assert collectOddValues([]) == []
assert collectOddValues([4.0]) == []

assert countInts([1,2,3,4,3,2,1], 2) == 2 #Professor's Example
assert countInts([2,2,3,4,6,7,3],7) == 1
assert countInts([],1) == 0
assert countInts([-1,-4,-100],-1) == 1
assert countInts([4.0,3,4,5.0],4) == 1

assert reverseString("CMPSC9") == "9CSPMC" #Professor's Example
assert reverseString("Hello") == "olleH"
assert reverseString("Hi My Name Is") == "sI emaN yM iH"
assert reverseString("") == ""
assert reverseString("    ") == "    "

assert removeSubString("Lolololol", "lol") == "Loo" #Professor's Example
assert removeSubString("My Pokemon Go", "kem") == "My Poon Go"
assert removeSubString("Ah, I love spiders!", "I love ") == "Ah, spiders!"
assert removeSubString("I can~~~~~t sing", "~") == "I cant sing"
assert removeSubString("f u           n", " ") == "fun"
assert removeSubString("I don't think this will remove anything", "z") == "I don't think this will remove anything"