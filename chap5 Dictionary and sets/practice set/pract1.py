myDict = {
    "Impossible": "The one that can't be ever performed",
    "Pre-executing": "Performing a task before hand",
    "Extinction": "Species that were never seen again",
    "Motivation": "Taking a point on positiveness"
}

print("Options are ", myDict.keys())
a = input("Enter the word\n")
# print("The meaning of your word is:", myDict[a])

# Bellow line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))
