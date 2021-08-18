def findFact(n):
    list = []
    for i in range(1,n+1):
        if n%i == 0 :
            list.append(i)
    return list


def isPrime(n):
    list = findFact(n)
    if len(list) == 2 :
        return True
    else :
        return False

def primeUpto(n):
    list = []
    for i in range(1,n+1):
        if isPrime(i) :
           list.append(i)
    return list

def primeproduct(n):
    list1 = primeUpto(n)
    for i in range(0, len(list1)):
        for j in range(i, len(list1)):
            print(list1[i]*list1[j])
            if list1[i]*list1[j] == n:
                print("True")
                return True
    print("False")
    return False

def delchar(s,c):
    newString = []

    for i in range(0,len(s)):
        if s[i]==c:
            continue
        newString.append(s[i])
    return ''.join(newString).replace(" ","")
def shuffle(l1,l2):
    newList = []
    count = len(l1)
    if len(l1)>len(l2):
        count = len(l2)
    l1Count = 0
    l2Count = 0
    for i in range(0,count*2):
        if i%2==0 :
            newList.append(l1[l1Count])
            l1Count = l1Count + 1
        else :
            newList.append(l2[l2Count])
            l2Count = l2Count + 1
    if len(l1)>len(l2):
        for i in range(l1Count,len(l1)):
            newList.append(l1[i])
    elif len(l2)>len(l1):
        for i in range(l2Count,len(l2)):
            newList.append(l2[i])
    else :
        print(newList)
        return newList
    print(newList)
    return newList

print(delchar("banana","a"))
