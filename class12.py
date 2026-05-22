#Exception handling
def divide():
 try:
  num1 = int(input("enter your first number"))
  num2 = int(input("enter your second number"))
  result = num1 / num2
  print("result:",result)
 except Exception as e:
  print(e)
  print("you have some issues on input")


# except ZeroDivisionError as e:
#  print(e)
#  print("you can not divide a number by zero")   
#  divide()

# except ValueError as e:
#  print(e)
#  print("you must enter a valid number")
#  divide()

