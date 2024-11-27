import csv

def read_csv(file_name):
    with open('username.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
