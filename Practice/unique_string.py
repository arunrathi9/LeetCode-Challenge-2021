# Q: Implement an algorithm to determine if a string has all unique characters.

# using extra data structure
# TC = O(n)
# SC = O(n)
def Is_unique(string):

    str_dict = dict()
    for key in string:
        if key in str_dict:
            return False
        else:
            str_dict[key] = 1
    
    return True

print(Is_unique('abcde'))
print(Is_unique('strings'))

# without using extra data structure
# TC = O(nlogn)
# SC = O(1)

def is_unique2(string):
    temp = sorted(string)

    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            return False
    
    return True

print(is_unique2('abcde'))
print(is_unique2('strings'))