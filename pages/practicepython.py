#python basic practice collections
from collections import Counter, defaultdict

print("lets start")

def isduplicatechar(string):
    seen = set()
    duplicatechar = False
    for char in string:
        if char not in seen:
            seen.add(char)
        else:
            print(char)
            duplicatechar = True
            return duplicatechar


#isduplicatechar("abcda")


def firstnonrepeatingchar(string):
    uniquechars = dict()
    for char in string:
        if char not in uniquechars:
            uniquechars[char] = 1
        else:
            uniquechars[char] += 1
    print(uniquechars.values())
    for char in string:
        if uniquechars[char] == 1:
            print("first character found",char)
            return char
    print("first character not found")
    return None
#firstnonrepeatingchar("aabbcc")

def firstrepeatingchar(string):
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
        else:
            print(char)
            return  char
    return None
#firstrepeatingchar("abcdefa")


def reversestring(string):
    emptylist = ""
    for char in string:
        emptylist =char + emptylist
    print(emptylist)


reversestring("vishal")

def finaanagram(string,string2):
    if len(string) == len(string2):
        temp1 = list(string)
        temp2 = list(string2)

        for char in temp1:
            if char in temp2:
                temp2.remove(char)
        assert len(temp2) <1
    else:
        print("string and string2 are different")

#finaanagram("listen","silent")


def two_sum_bruteforce(nums,target):
   for i in range(len(nums)):
       for j in range(i+1,len(nums)):
           if nums[i]+nums[j] == target:
               print(i,j)
               return i,j
   return None


#two_sum_bruteforce([6,7,8,9,33,5],38)


#try using without set
def removeduplicatenum(nums):
    seen = set(nums)
    print(seen)
    for num in nums:
        seen.add(num)
    print(seen)

#removeduplicatenum([2,3,4,5,5,3,2,1])


def findmissingnumber(nums):
    tempnums = sorted(nums)
    i=tempnums[0]
    print(i)
    for num in tempnums:
        if num == i:
            i += 1
        else:
            print("missing number found",i)
            return i
    return None


findmissingnumber([9,6,5,10,8,11])

def findtopknumbers(k,data):
    freq = Counter(data)
    top_k =freq.most_common(k)
    print(top_k)
    return " ".join(f"{num},{count}" for num, count in top_k)


#print(findtopknumbers(3,[1,1,1,2,2,3,4,4,4,7,7,7,7,7]))

def finddifftwoarray(list1,list2):
    result = []

    for num in list1:
        if num not in list2:
            result.append(num)
    for num in list2:
        if num not in list1:
            result.append(num)
    print(result)


#finddifftwoarray(list1=[2,3,4,5],list2=[1,2,3,4,5,6])

def groupanagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word)) # sort letter to form a key
        anagrams[key].append(word)

    return list(anagrams.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupanagrams(words))