from faker import Faker
import csv

fake = Faker()

def generate_data(num):
    data = []
    for i in range(num):
        name = fake.name()
        hiring_date = fake.date_between(start_date='-10y', end_date='today')
        department = fake.job()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=75)
        data.append([name, hiring_date, department, birthday])
    return data

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Hiring Date", "Department", "Birthday"])
        writer.writerows(data)



if __name__ == "__main__":
    employee_data = generate_data(20)
    write_to_csv(employee_data, 'database.csv')
