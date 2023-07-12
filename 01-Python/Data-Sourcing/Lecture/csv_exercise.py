import csv

# with open('data/addresses.csv') as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     #print(reader)
#     for row in reader:
#         # row is a `list`
#         print(row[1])

# import csv

# with open('data/biostats.csv') as csv_file:
#     reader = csv.DictReader(csv_file, skipinitialspace=False)
#     for row in reader:
#          # row is a dict
#         print(row)
#         #print(row['Name'], row['Sex'], int(row['Age']))

beatles = [
    { 'first_name': 'John', 'last_name': 'lennon', 'instrument': 'guitar'},
    { 'first_name': 'Ringo', 'last_name': 'Starr', 'instrument': 'drums'}
]



with open('data/beatles.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
    writer.writeheader()
    for beatle in beatles:
          writer.writerow(beatle)
