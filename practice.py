# ------------------------------
# 1. Character Frequency
# Problem: Count how many times each character appears in the string s
# Example: "banana" -> {'b': 1, 'a': 3, 'n': 2}
# ------------------------------
def characterFrequency(s: str) -> dict:
    my_map = {}
    
    for char in s:
        if char not in my_map:
            my_map[char] = 1
        else:
            my_map[char] += 1
    return my_map

# Example call
print("1. Character Frequency:", characterFrequency("banana"))


# ------------------------------
# 2. First Unique Character
# Problem: Return the first character in s that appears only once
# Example: "swiss" -> "w"
# ------------------------------
def firstUniqueChar(s: str):
    my_map = {}

    for char in s:
        if char not in my_map:
            my_map[char] = 1
        else:
            my_map[char] +=1

    for char in s:
        if my_map[char] == 1:
            return char
        
    return None

  
# Example call
print("2. First Unique Character:", firstUniqueChar("swiss"))


# ------------------------------
# 3. Contains Duplicate
# Problem: Return True if any element appears more than once in nums
# Example: [1, 2, 3, 4, 2] -> True
# ------------------------------
def containsDuplicates(nums: list) -> bool:
    my_map = {}

    for num in nums:
        if num not in my_map:
            my_map[num] = 1
        else:
            return False
    return True

   
# Example call
print("3. Contains Duplicates:", containsDuplicates([1, 2, 3, 4, 2]))


# ------------------------------
# 4. Group Words by Length
# Problem: Group words by length in a dictionary {length: [words]}
# Example: ["cat", "hi", "bear", "dog"] -> {2: ["hi"], 3: ["cat", "dog"], 4: ["bear"]}
# ------------------------------
def groupByLength(words: list) -> dict:
    my_map = {}

    for word in words: 
        l = len(word)
        if l not in my_map:
            my_map[l] = [word]
        else:
            my_map[l].append(word)
    return my_map
    

# Example call
print("4. Group Words by Length:", groupByLength(["cat", "hi", "bear", "dog", "candy"]))


# ------------------------------
# 5. Common Elements in Two Lists
# Problem: Return a list of elements present in both lists (no duplicates)
# Example: [1,2,3], [2,3,4] -> [2, 3]
# ------------------------------
def commonElements(li1: list, li2: list) -> list:
    # set1 = set(li1)
    # set2 = set(li2)

    # return list(set1.intersection(set2))
    my_map = {}
    res = set()
    for num in li1:
        if num not in my_map:
            my_map[num] = 1
        else:
            my_map[num] += 1

    for num in li2:
        if num in my_map:
            res.add(num)
    return list(res)
  


# Example call
print("5. Common Elements:", commonElements([1,2,3,5], [2,3,4,2]))


# ------------------------------
# 6. Are Anagrams
# Problem: Return True if str1 and str2 are anagrams
# Example: "listen", "silent" -> True
# ------------------------------
def isAnagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2): return False

    my_map = {}

    for char in str1:
        if char not in my_map:
            my_map[char] = 1
        else:
            my_map[char] +=1
    
    for char in str2:
        if char not in my_map or my_map[char] == 0:
            return False
        else:
            my_map[char]-=1
    return True
# Example call
print("6. Are Anagrams:", isAnagram("listenn", "silent"))


# ------------------------------
# 7. Most Frequent Element
# Problem: Return the element that appears most frequently in nums
# Example: [1,2,2,3,3,3] -> 3
# ------------------------------
def mostFreq(nums: list):
    my_map = {}
    freq = 0

    for num in nums:
        if num not in my_map:
            my_map[num] = 1
        else:
            my_map[num] += 1
        freq = max(freq, my_map[num])
    
    return my_map.get(freq)
        


# Example call
print("7. Most Frequent Element:", mostFreq([1,2,2,3,3,3, 3]))
