
#numbers.clear()
#numbers.append(200)
#del numbers[2]
#del numbers 

    


fruits = ["apple,","banana","cherry","pine","ornAge"]
value = list(fruits)
for x in value:
    if "a" in x.lower():
       value.remove(x)
print("value:",value)





number = [1,2,3,4,5,6,7,8]

for w in range(len(number)):
   if number[w] % 2 == 0:
      number[1]="EVEN"
print("number:", number)


fruits = [ "apple","banana", "cherry","ggg", "fff", "hhh"] #scan above list and remove the  non vowel fromt the fruits 
filtered_fruits = list(fruits)
vowels = "aeiou"

for value in fruits:
   flag = False
   for x in value:
      if x.lower() in vowels:
           flag = True
           break
      if flag:
         filtered_fruits.remove(value)

print("filtered_fruits",filtered_fruits)         


numbers = (1,1,1,2,3,4,5,3)
new_numbers = list(numbers)
for x in numbers:
    if numbers.count(x) > 1:
        for y in range(number.count(x)-1):

         new_numbers.remove()

matrix = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
value = matrix[0]
value1 = value[1]

print(value1)


value = matrix[0][1]


product = 1  

for i in range(len(matrix)):
   product *= matrix[i][i]

print("product:",product)

product = 1
c = len(matrix)




