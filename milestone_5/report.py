import csv
import sys
from datetime import datetime


def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')


def count_presents(database_file, month):
    birthday_presents = 0
    anniversary_presents = 0

    with open(database_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            birthday_date = parse_date(row['Birthday'])
            anniversary_date = parse_date(row['Hiring Date'])

            if birthday_date.month == month:
                birthday_presents += 1
            if anniversary_date.month == month:
                anniversary_presents += 1

    return birthday_presents, anniversary_presents
def main(database_file, month):
    birthday_presents, anniversary_presents = count_presents(database_file, month)

    print(f'Presents needed for birthdays in month {month}: {birthday_presents}')
    print(f'Presents needed for hiring anniversaries in month {month}: {anniversary_presents}')
    print(f"Total presents in month {month}: {birthday_presents + anniversary_presents}")

if __name__ == "__main__":
    month = int(input("Enter the month number: "))
    main("database.csv", month)