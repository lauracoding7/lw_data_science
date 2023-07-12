import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file) # reader returns a list
    line_count = 0
    for row in csv_reader:
        # ROW IS LIST
        print(row)
        line_count += 1

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True) # DictReader returns a dictionary

    for row in csv_reader:
        # ROW IS DICTIONARY
        print(f"{row['last_name']}: {row['phone_number']}")
