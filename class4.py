s = "Hello, world!"

print(s.replace("world","python"))

s = "Hello, World!"

print (s.lower())


s = "Hello, World!"

print (s.upper())


s = "hello, world!"

print(s.title())


s = "   Hello, World!"
print(s.Lstrip(s))


s = "   Hello, World!   "
print(s.rstrip())


s = "   Hello, World!    "
print(s.strip())


name = "######hello, world####"

print(name.strip("#"))


Name = "Hello#World"

value = name.split("#")
print(value)

s = "1,2,3,4,5"
print(s.isdigit())

s = "HELLO, WORLD!"
print(s.isupper())

name1 = input("enter your name")
name2 = input("enter your name")

value = "Hello! {}.Hi {}".format(name1,name2)
print("Hello! {}.Hi []".format(name1,name2))

