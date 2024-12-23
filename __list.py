# List Operations


# List Addition
list_1 = ['apple', 'banana', 'orange']  # Initial list




# Adding elements to the list
list_1.append("grape")  # Adds "grape" to the end of the list
list_1.insert(2, "kiwi")  # Inserts "kiwi" at index 2 (third position)




# List Update
list_1 = ['apple', 'banana', 'orange']  # Re-initializing the list
list_1[1] = 'watermelon'  # Updates the second element (index 1) to "watermelon"




# List Sort
list_2 = [1, 2, 4, 7, 6, 5, 8, 3]  # Unsorted list
list_2.sort()  # Sorts the list in ascending order
print(list_2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]



# List Deletion
list_3 = ['a', 'g', 'd', 'r', 'y']  # Initial list




# Deleting elements from the list
list_3.pop()      # Removes the last element ('y')
list_3.pop(2)    # Removes the element at index 2 ('d')
del list_3[2]    # Also removes the element at index 2 (after previous pop)
list_3.remove('a')  # Removes the first occurrence of 'a'




# List Extend
present = ['arya', 'hosna', 'mohamad hosein']  # Present students
apsent = ['helma', 'amir', 'ali']               # Absent students
present.extend(apsent)  # Extends present list with absent students
# Result: ['arya', 'hosna', 'mohamad hosein', 'helma', 'amir', 'ali']




# List Clear
list_4 = [1, 4, 8, 12, 16]   # Initial list
list_4.clear()               # Clears all elements from the list
del list_4                   # Deletes the list entirely