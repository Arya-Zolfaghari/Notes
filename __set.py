# set : 
#      unordred / unidexed / unchangeable / not allow duplicate / add item 
# 1 = True
# 2 = Fals

# ordred is not sort


theset = {"amir","arya","mohammad"} # making Set

# outpot  ==>  the objects have random index  

print(theset)

print("arya" in theset)  #  ==> True


################################################################


# add/remove/coppy item

myset=theset.copy()

theset.add("mamad") # add

theset.remove("amir") # remove amir
theset.discard("amir") # remove amir
theset.pop() # remove the last one
theset.clear() # clear the set and meke it to empty
del myset #  delete the hole set

#################################################################

# update

theset2 = {"hosein" , "farid" , "asghar"}

theset.update(theset2)
# theset + theset2 = theset
theset3 = theset.union(theset2)
# theset + theset2 = theset

x={1,2,3,4,5}
y={1,4,7,9,6}

x.intersection_update(y) # x & y
# hold the same object in the sets
z=x.intersection(y) # x & y
# hold the same object in the sets

x.symmetric_difference_update(y) # x | y
# hold the not same object in the sets
z=x.symmetric_difference(y) # x | y
# hold the not same object in the sets


