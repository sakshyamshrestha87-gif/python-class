# def greeting(name):
#     print("Hello,"  + name)

# def sum(a,b):
#     result =  a+b
#     print("result",result)
#     return result

# def diff(a,b):
#     result = a-b
#     print("result",result)
#     return result

# def ml(a,b):
#     result = a*b
#     print("result",result)
#     return result

# #method1


# import mymodule

# mymodule.greeting("ram")
# #method2



# import mymodule as m

# m.greeting("hari")

# #method3

# from mymodule import greeting,add


# greeting("shhyam")

# add(1,2)


# #method4
# from mymodule import greeting as g,add as a

# g("shyam")
# a(1,2)

#without parameter function and without parameter decorator
def decorator(x):
    def wrapper():
        print("something before function runs")

        x()

        print("hi")
        print("bye")
    return wrapper

@decorator
def say_hello():

    print("hello")

say_hello()
    






