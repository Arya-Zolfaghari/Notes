# 1:

# when ever we open a file we are taking the hole code in the variable and we will use it
my_file = open("==Note==/files_in_python/students.txt" , "r")
#                name           mode

print(type(my_file))
# output => <class '_io.TextIOWrapper'>


print(my_file)
# Output => <_io.TextIOWrapper name='students.txt' mode='r' encoding='cp1252'>






# read 


print(my_file.readline()) # read the first line of the file


print(my_file.readable())
# Output => True because the mode of my_file is "r"


print(my_file.readlines()) # the list of the value of files 
 #['amirali\n', 'arya\n', 'mohammad hossein\n', 'hosna\n', 'aynaz\n', 'ali']

# remove \n in list    .split
text = "1.2.3.4.5" 
# output : 1 2 3 4 5 

print(text.split("."))
# Output : ['1', '2', '3', '4', '5']
# it remove sth in str and change the type to list









my_file.close()






# 2 : here you shouldnt close your file

try:
    with open("==Note==/files_in_python/students.txt" , "r") as my_file : 
        print(my_file)
        for line in my_file:
            print(line)
except:
    print("an eror occures duringopening file .")









# write file 

with open('test.txt','w') as file:
    file .write(" welcome to the py class\n")
    
    
    
    
    
# append => a
with open("==Note==/files_in_python/test.txt" , "a")as file :
    file.write("helma\n")
    file.writelines("ali\n amir\n")
    # it will write them in the test.txt
    
    



# remove file :
import os 
# operating system 
if os.path.exists("test.txt"):
    os.removedirs("test.txt")
else : print("the file does not exists")



##############################################
# reletive path
with open("=Note=/files_in_python/students.txt" , "r") as reader :
    print(reader.read())
    
# files_in_python ==> __files in python .copy()
# =Note=  ==>  students.txt
open("../students.txt") # go out of here



# read 2 files 

#  first 
file_data = None

with open("students.txt" , "r") as reader :
    file_data = reader.read()
    
with open("test.txt" , "w") as writer :
    writer.write(file_data)

# seccond best

with open("students.txt" , "r") as reader , open("test.txt" , "w") as writer :
    writer.write(reader.read())



