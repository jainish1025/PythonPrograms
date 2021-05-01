myDict = {
    "jack": "A coder",
    "fast": "In a quick manner",
    "marks": [1, 2, 3],
    "anotherdict": {'jack': 'player'},
    1: 2
}

# Dictionary methods

# print(list(myDict.keys())) #print the keys of the dictionary
# print(myDict.values()) #print the keys of the dictionary
# print(myDict.items()) #print the (keys,value) for all contents of the dictionary
# print(myDict)
# updateDict={
#     "Lovish":"Friend",
#     "jack":"Gamer"
# }
# myDict.update(updateDict) #update the ductionary by adding key-value pair from updateDict
# print(myDict)

print(myDict.get("jack"))  # print value associated with key a "jack"
print(myDict["jack"])  # print value asspciated with key "jack"

# The difference between .get and [] system in dictionaries
# Returns None as Jack2 is not present in dictionary
print(myDict.get("jack2"))
print(myDict["jack2"])  # throw an error as jack2 is not in the dictionary
