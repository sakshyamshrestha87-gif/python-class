#with open("file.txt","a") as f:
#    for i in range(5):
#        row = f.write(f"index : {i}\n")
#        print(row)



import csv

#file_path = 'data.csv'

#with open(file_path, mode='r') as file:
#    csv_reader = csv.reader(file)
#    header = next(csv_reader )
#    for row in csv_reader:
#        print(row,{1})

data = [
    ['Alice', 30, 'london'],
    ['bob', 24, 'paris'],
    ['charlie', 35, 'berlin']
]
file_path = 'output.csv'

with open(file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow('Age')
    for row in data:
        csv_writer.writerow(row)
        print(csv_writer.writerow)