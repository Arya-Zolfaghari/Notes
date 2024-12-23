mylist = [1,2,3,4,5,6]
mylist2 = [-1,-2,-3,-4,-5,-6]


def myfunc(number):
          return number * 2

# map ( function  ,   iterable)
x=map(myfunc , mylist)
# ==>
# for item in mylist:
#           print(item)

print(list(x)) 
# outpot ==> 2,4,6,8,10,12


x=list(map(lambda a, b  : a * b, mylist , mylist2))
print(x)
# forever

x=map(lambda a, b  : a * b, mylist , mylist2)
print(list(x))
# for onetime