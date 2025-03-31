import csv

file_name = 'AAPL.csv'

fields = []
rows = []

with open(file_name, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    fields.append(next(csv_reader))

    for row in csv_reader:
        rows.append(row)

    print("Total rows in the file is:", csv_reader.line_num)

    for x in rows:
        print(x)
