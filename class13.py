#file handling

#file_path = "demofile.txt"
#with open(file_path, 'r')  as file:
#    content = file.read()
#    print(content)


#f = open("demofile.txt","r")
#value = f.read()
#print(value)
#f.close()

#with open("demofile.txt","r") as f:
#    value = f.read()
#    print(value)
#    print(type(value))


#f = open("demofile.txt","r")
#c = open("demofile.txt","w")

#value = f.read()
#for i in value:
#    c = c+1
#    if value = "hello"
#        f.read("")

value = """ Hello! Welcoome to demofile.txt
this file is for testing purposes
Good luck"""

with open("demofile.txt","r") as f:
    row = f.readline()
    row132 = f.readline()
    for x in f:
     print(x)

with open("demofile.txt","r") as f:
    row = f.readlines()
    print(row)




