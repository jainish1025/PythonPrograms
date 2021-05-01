## Creating  an empty set
b = set()
print(type(b))

##Adding value to as empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set.
b.add((4, 5, 6))

## Accessing Elements
# b.add({5:7}) # cannot add list or dictionary in set.
print(b)

##Length of the set
print(len(b)) # print the length of this set

##Remove of an items
b.remove(5)
# b.remove(15) # Throw an error while tying to remove 15(which is not presend in the set)
print(b)

print(b.pop())
print(b)