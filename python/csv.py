import csv
with open('d:\python\student.csv','r')as file:
    reader=csv.reader(file,delimiter='\t')
    for row in reader:
        print(row)
