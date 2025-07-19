import csv
from utils import (
    add_expense,
    read_all_expenses,
    calculate_total,
    filter_by_date,
    filter_by_category,
    format_expense
)

def handle_add_expense(date, category, amount):
    date = input(" Harajat sanasini kiriting (YYYY-MM-DD): ")
    category = input(" Harajat kategoriyasini kiriting: ")
    amount = float(input(" Harajat miqdorini kiriting: "))
    
    expense = add_expense(date, category, amount)
    if expense:
        print(f" Harajat qo'shildi: {format_expense(expense)}")
    else:
        print(" Harajat qo'shishda xatolik yuz berdi.")

def handle_view_all(date=None, category=None):
    expenses = read_all_expenses(date, category)
    print("Barcha harajatlar:")
    print(expenses)

def handle_total(expenses=None):
    expenses = calculate_total(expenses)
    print(f" Jami harajatlar: {expenses}")

def handle_filter_by_date(expenses=None):
    search_date = input("📅 Qidirilayotgan sanani kiriting (YYYY-MM-DD): ")
    expenses = filter_by_date(expenses, search_date)
    print(f"Sanaga ko'ra filtrlangan harajatlar:{expenses}")

def handle_filter_by_category(expenses=None):
    search_category = input(" Qidirilayotgan kategoriya nomini kiriting: ")
    expenses = filter_by_category(expenses, search_category)
    print(f"Kategoriyaga ko'ra filtrlangan harajatlar: {expenses}")

def main():
    while True:
        print("\n📋 Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Filter by Date")
        print("5. Filter by Category")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            handle_add_expense(date=None, category=None, amount=None)
        elif choice == "2":
            handle_view_all()
        elif choice == "3":
            handle_total(expenses=None)
        elif choice == "4":
            handle_filter_by_date(expenses=None)
        elif choice == "5":
            handle_filter_by_category(expenses=None)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
