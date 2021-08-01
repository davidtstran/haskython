# python conversion for haskell-example.hs

def incList(integer: list[int]) -> int:  
    if integer == []: 
        return []
    else:
        returnList = [integer[0]+1]
        returnList.extend(incList(integer[1:]))
        return returnList

print(incList([1,2,3])) # [2,3,4]

def decList(integer: list[int]) -> int:  
    if integer == []: 
        return []
    else:
        returnList = [integer[0]-1]
        returnList.extend(decList(integer[1:]))
        return returnList

print(decList([1,2,3])) # [0,1,2]

def sumList(integer: list[int]) -> int:
    if integer == []: 
        return 0
    else:
        return integer[0] + sumList(integer[1:])

print(sumList([1,2,3])) # 6

def power(integer: int, integer1: int) -> int:
    if integer1 == 0:
        return 1
    elif integer1 == 1:
        return integer
    else: 
        return integer * power(integer, integer1-1)

print(power(2, 3)) # 8