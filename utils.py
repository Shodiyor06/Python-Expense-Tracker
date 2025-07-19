import csv

FILENAME = "expenses.csv"

def add_expense(date, category, amount):
    
    with open(FILENAME, "a") as file:
        file.write(f"{date},{category},{amount}\n")
    return (date, category, amount)

def read_all_expenses(date, category):
    with open(FILENAME, "r") as file:
        expenses = [line.strip().split(",") for line in file.readlines()]
    return expenses


def calculate_total(expenses):
    with open(FILENAME, "r") as file:
        expenses = list(csv.reader(file))
        n = 0
        for i in expenses:
            if float(i[2]) != 0:
                n += float(i[2])          
    return n

def filter_by_date(expenses, search_date):
    with open(FILENAME, "r") as file:
        expenses = list(csv.reader(file))
        lst = []
        for i in expenses:
            if i[0] == search_date:
                lst.append(i)
        return lst
    
def filter_by_category(expenses, search_category):
    with open(FILENAME, "r") as file:
        expenses = list(csv.reader(file))
        lst = []
        for i in expenses:
            if i[1] == search_category:
                lst.append(i)
        return lst

def format_expense(row):
    return f" {row[0]} | {row[1]} |  {row[2]}"
