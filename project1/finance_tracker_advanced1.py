import sqlite3
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_FILE = "finance_tracker.db"

# ---------------- Database Setup ---------------- #
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
            recurring TEXT DEFAULT NULL,  -- e.g., 'monthly', 'weekly'
            budget_limit REAL DEFAULT NULL
        )
    """)
    conn.commit()
    conn.close()

# ---------------- Transaction Management ---------------- #
def add_transaction(amount, category, t_type, date, recurring=None, budget_limit=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO transactions (amount, category, date, type, recurring, budget_limit) VALUES (?, ?, ?, ?, ?, ?)",
        (amount, category, date, t_type, recurring, budget_limit)
    )
    conn.commit()
    conn.close()
    print("✅ Transaction added successfully!")

def view_transactions(start_date=None, end_date=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    query = "SELECT date, type, category, amount FROM transactions"
    params = []
    if start_date and end_date:
        query += " WHERE date BETWEEN ? AND ?"
        params = [start_date, end_date]
    query += " ORDER BY date ASC"
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    if rows:
        print(f"{'Date':<12} {'Type':<8} {'Category':<15} {'Amount':<10}")
        print("-"*50)
        for row in rows:
            print(f"{row[0]:<12} {row[1]:<8} {row[2]:<15} {row[3]:<10.2f}")
    else:
        print("No transactions found for the given period.")

def financial_summary(start_date=None, end_date=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    query = "SELECT type, SUM(amount) FROM transactions"
    params = []
    if start_date and end_date:
        query += " WHERE date BETWEEN ? AND ?"
        params = [start_date, end_date]
    query += " GROUP BY type"
    c.execute(query, params)
    results = dict(c.fetchall())
    conn.close()
    total_income = results.get("income", 0)
    total_expense = results.get("expense", 0)
    net_balance = total_income - total_expense
    print("\n📊 Financial Summary:")
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Net Balance:    ${net_balance:.2f}")

def category_breakdown(start_date=None, end_date=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    query = "SELECT category, SUM(amount) FROM transactions WHERE type='expense'"
    params = []
    if start_date and end_date:
        query += " AND date BETWEEN ? AND ?"
        params = [start_date, end_date]
    query += " GROUP BY category"
    c.execute(query, params)
    results = c.fetchall()
    conn.close()
    if results:
        print("\n📂 Expenses by Category:")
        for cat, amt in results:
            print(f"{cat:<15}: ${amt:.2f}")
    else:
        print("No expenses recorded for the given period.")

# ---------------- Charts ---------------- #
def plot_summary(start_date=None, end_date=None):
    conn = sqlite3.connect(DB_FILE)
    query = "SELECT type, SUM(amount) FROM transactions"
    params = []
    if start_date and end_date:
        query += " WHERE date BETWEEN ? AND ?"
        params = [start_date, end_date]
    query += " GROUP BY type"
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    if not df.empty:
        plt.figure(figsize=(6,6))
        plt.pie(df['SUM(amount)'], labels=df['type'], autopct='%1.1f%%', colors=['green','red'])
        plt.title('Income vs Expenses')
        plt.show()
    else:
        print("No data to plot.")

def plot_category_breakdown(start_date=None, end_date=None):
    conn = sqlite3.connect(DB_FILE)
    query = "SELECT category, SUM(amount) FROM transactions WHERE type='expense'"
    params = []
    if start_date and end_date:
        query += " AND date BETWEEN ? AND ?"
        params = [start_date, end_date]
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    if not df.empty:
        plt.figure(figsize=(8,6))
        plt.bar(df['category'], df['SUM(amount)'], color='orange')
        plt.title('Expenses by Category')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("No expenses to plot.")

# ---------------- Recurring Transactions ---------------- #
def process_recurring():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    today = datetime.today().strftime("%Y-%m-%d")
    c.execute("SELECT id, amount, category, type, recurring, date FROM transactions WHERE recurring IS NOT NULL")
    recurring_transactions = c.fetchall()
    for tx in recurring_transactions:
        tx_id, amount, category, t_type, recurring, date_str = tx
        last_date = datetime.strptime(date_str, "%Y-%m-%d")
        today_dt = datetime.today()
        while last_date < today_dt:
            if recurring == 'monthly':
                last_date += timedelta(days=30)
            elif recurring == 'weekly':
                last_date += timedelta(days=7)
            if last_date <= today_dt:
                add_transaction(amount, category, t_type, last_date.strftime("%Y-%m-%d"), recurring)
    conn.close()

# ---------------- Budget Alerts ---------------- #
def check_budget_alerts():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount), budget_limit FROM transactions WHERE type='expense' AND budget_limit IS NOT NULL GROUP BY category")
    alerts = c.fetchall()
    for cat, spent, limit in alerts:
        if spent > limit:
            print(f"⚠️ Alert: Spending in '{cat}' exceeded the budget of ${limit:.2f} (Spent: ${spent:.2f})")
    conn.close()

# ---------------- CLI Input ---------------- #
def get_transaction_input():
    while True:
        try:
            t_type = input("Enter type (income/expense): ").strip().lower()
            if t_type not in ["income", "expense"]:
                raise ValueError("Type must be 'income' or 'expense'")
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Salary, Groceries): ").strip()
            date_input = input("Enter date (YYYY-MM-DD) or leave empty for today: ").strip()
            date = date_input if date_input else datetime.today().strftime("%Y-%m-%d")
            datetime.strptime(date, "%Y-%m-%d")
            recurring = input("Recurring? (none/monthly/weekly): ").strip().lower()
            recurring = recurring if recurring in ['monthly','weekly'] else None
            budget_limit = None
            if t_type == 'expense':
                budget_input = input("Set budget limit for this category (optional): ").strip()
                if budget_input:
                    budget_limit = float(budget_input)
            return amount, category, t_type, date, recurring, budget_limit
        except ValueError as e:
            print(f"⚠️ Invalid input: {e}. Please try again.")

def get_date_range():
    while True:
        try:
            start = input("Start date (YYYY-MM-DD): ").strip()
            end = input("End date (YYYY-MM-DD): ").strip()
            datetime.strptime(start, "%Y-%m-%d")
            datetime.strptime(end, "%Y-%m-%d")
            return start, end
        except ValueError:
            print("⚠️ Invalid date format. Please try again.")

# ---------------- Main CLI ---------------- #
def main():
    init_db()
    process_recurring()  # Ensure recurring transactions are up to date
    while True:
        check_budget_alerts()  # Check for overspending alerts
        print("\n=== Advanced Finance Tracker ===")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Financial Summary")
        print("4. Expense Breakdown by Category")
        print("5. View Transactions by Date Range")
        print("6. Financial Summary by Date Range")
        print("7. Plot Income vs Expenses")
        print("8. Plot Expenses by Category")
        print("9. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            amount, category, t_type, date, recurring, budget_limit = get_transaction_input()
            add_transaction(amount, category, t_type, date, recurring, budget_limit)
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            financial_summary()
        elif choice == "4":
            category_breakdown()
        elif choice == "5":
            start, end = get_date_range()
            view_transactions(start, end)
        elif choice == "6":
            start, end = get_date_range()
            financial_summary(start, end)
        elif choice == "7":
            start_range = input("Start date (YYYY-MM-DD) or leave empty: ").strip()
            end_range = input("End date (YYYY-MM-DD) or leave empty: ").strip()
            start_date, end_date = (start_range, end_range) if start_range and end_range else (None, None)
            plot_summary(start_date, end_date)
        elif choice == "8":
            start_range = input("Start date (YYYY-MM-DD) or leave empty: ").strip()
            end_range = input("End date (YYYY-MM-DD) or leave empty: ").strip()
            start_date, end_date = (start_range, end_range) if start_range and end_range else (None, None)
            plot_category_breakdown(start_date, end_date)
        elif choice == "9":
            print("Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
