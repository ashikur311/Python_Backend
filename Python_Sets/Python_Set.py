# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.
# Sets cannot have two items with the same value.
fruits={"apple", "banana", "cherry","apple","cherry","orange","kiwi","mango","papaya"}
print(fruits)  # Duplicate values will be removed


# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Once a set is created, you cannot change its items, but you can add new items.
fruits.add("grape")
print("Set after adding grape:", fruits)

#To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print("Set after updating with tropical fruits:", fruits)

#Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
mylist = ["kiwi", "watermelon"]
fruits.update(mylist)
print("Set after updating with a list:", fruits)

#To remove an item in a set, use the remove(), or the discard() method.
fruits.remove("banana")
print("Set after removing banana:", fruits)
fruits.discard("orange")
print("Set after discarding orange:", fruits)
#Note: If the item to remove does not exist, remove() will raise an error.
# discard() will NOT raise an error.

#The clear() method empties the set:
fruits.clear()
print("Set after clearing all items:", fruits)

#The del keyword will delete the set completely:
del fruits
# print(fruits)  # This will raise an error because the set no longer exists.

#Set operations
A = {"apple", "banana", "cherry"}
B = {"google", "microsoft", "apple"}
#The union() and update() methods joins all items from both sets.
C = A.union(B)
print("Union of A and B:", C)
#The intersection() method keeps ONLY the duplicates.
D = A.intersection(B)
print("Intersection of A and B:", D)

#The difference() method keeps the items from the first set that are not in the other set(s).
E = A.difference(B)
print("Difference of A and B (A-B):", E)
F = B.difference(A)
print("Difference of B and A (B-A):", F)
#The symmetric_difference() method keeps all items EXCEPT the duplicates.
G = A.symmetric_difference(B)
print("Symmetric Difference of A and B:", G)
#Set Membership Test
print("Is 'banana' in set A?", "banana" in A)
print("Is 'microsoft' in set A?", "microsoft" in A)