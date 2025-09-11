import sqlite3
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
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
            recurring TEXT DEFAULT NULL,
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
    messagebox.showinfo("Success", "✅ Transaction added successfully!")
    update_table()
    check_budget_alerts()

def get_all_transactions(start_date=None, end_date=None):
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
    return rows

def financial_summary(start_date=None, end_date=None):
    rows = get_all_transactions(start_date, end_date)
    total_income = sum(r[3] for r in rows if r[1] == "income")
    total_expense = sum(r[3] for r in rows if r[1] == "expense")
    net_balance = total_income - total_expense
    messagebox.showinfo("Financial Summary",
                        f"Total Income: ${total_income:.2f}\n"
                        f"Total Expenses: ${total_expense:.2f}\n"
                        f"Net Balance: ${net_balance:.2f}")

def category_breakdown(start_date=None, end_date=None):
    rows = get_all_transactions(start_date, end_date)
    breakdown = {}
    for r in rows:
        if r[1] == "expense":
            breakdown[r[2]] = breakdown.get(r[2], 0) + r[3]
    if breakdown:
        msg = "\n".join([f"{cat}: ${amt:.2f}" for cat, amt in breakdown.items()])
        messagebox.showinfo("Expense Breakdown", msg)
    else:
        messagebox.showinfo("Expense Breakdown", "No expenses recorded.")

# ---------------- Charts ---------------- #
def plot_summary(start_date=None, end_date=None):
    rows = get_all_transactions(start_date, end_date)
    if rows:
        df = pd.DataFrame(rows, columns=["date","type","category","amount"])
        summary = df.groupby("type")["amount"].sum()
        plt.figure(figsize=(6,6))
        plt.pie(summary, labels=summary.index, autopct='%1.1f%%', colors=['green','red'])
        plt.title('Income vs Expenses')
        plt.show()
    else:
        messagebox.showinfo("Chart", "No data to plot.")

def plot_category_breakdown(start_date=None, end_date=None):
    rows = get_all_transactions(start_date, end_date)
    if rows:
        df = pd.DataFrame(rows, columns=["date","type","category","amount"])
        df = df[df['type']=='expense'].groupby('category')['amount'].sum()
        if not df.empty:
            plt.figure(figsize=(8,6))
            plt.bar(df.index, df.values, color='orange')
            plt.title('Expenses by Category')
            plt.ylabel('Amount ($)')
            plt.xticks(rotation=45)
            plt.show()
        else:
            messagebox.showinfo("Chart", "No expenses to plot.")
    else:
        messagebox.showinfo("Chart", "No data to plot.")

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
    c.execute("""
        SELECT category, SUM(amount), budget_limit
        FROM transactions
        WHERE type='expense' AND budget_limit IS NOT NULL
        GROUP BY category
    """)
    alerts = c.fetchall()
    conn.close()
    for cat, spent, limit in alerts:
        if spent > limit:
            messagebox.showwarning("Budget Alert",
                                   f"⚠️ Spending in '{cat}' exceeded the budget of ${limit:.2f} (Spent: ${spent:.2f})")

# ---------------- GUI Input Functions ---------------- #
def add_transaction_ui():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        t_type = type_var.get()
        date = date_entry.get() or datetime.today().strftime("%Y-%m-%d")
        recurring = recurring_var.get() if recurring_var.get() != "none" else None
        budget_limit = float(budget_entry.get()) if budget_entry.get() else None
        add_transaction(amount, category, t_type, date, recurring, budget_limit)
        clear_inputs()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for amount and budget.")

def clear_inputs():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    budget_entry.delete(0, tk.END)
    recurring_var.set("none")

def update_table():
    for row in tree.get_children():
        tree.delete(row)
    rows = get_all_transactions()
    for r in rows:
        tree.insert("", tk.END, values=r)

def filter_date_range():
    start = start_entry.get()
    end = end_entry.get()
    rows = get_all_transactions(start, end)
    for row in tree.get_children():
        tree.delete(row)
    for r in rows:
        tree.insert("", tk.END, values=r)

# ---------------- GUI Setup ---------------- #
root = tk.Tk()
root.title("Advanced Finance Tracker")
root.geometry("900x600")

# Input Frame
input_frame = tk.Frame(root, pady=10)
input_frame.pack()

tk.Label(input_frame, text="Type:").grid(row=0, column=0)
type_var = tk.StringVar(value="income")
ttk.Combobox(input_frame, textvariable=type_var, values=["income","expense"]).grid(row=0, column=1)

tk.Label(input_frame, text="Amount:").grid(row=1, column=0)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Category:").grid(row=2, column=0)
category_entry = tk.Entry(input_frame)
category_entry.grid(row=2, column=1)

tk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=3, column=0)
date_entry = tk.Entry(input_frame)
date_entry.grid(row=3, column=1)

tk.Label(input_frame, text="Recurring:").grid(row=4, column=0)
recurring_var = tk.StringVar(value="none")
ttk.Combobox(input_frame, textvariable=recurring_var, values=["none","weekly","monthly"]).grid(row=4, column=1)

tk.Label(input_frame, text="Budget Limit:").grid(row=5, column=0)
budget_entry = tk.Entry(input_frame)
budget_entry.grid(row=5, column=1)

tk.Button(input_frame, text="Add Transaction", command=add_transaction_ui).grid(row=6, column=0, columnspan=2, pady=5)

# Table Frame
table_frame = tk.Frame(root)
table_frame.pack()
tree = ttk.Treeview(table_frame, columns=("Date","Type","Category","Amount"), show="headings", height=15)
for col in ("Date","Type","Category","Amount"):
    tree.heading(col, text=col)
tree.pack()

# Summary and Filter Frame
summary_frame = tk.Frame(root, pady=10)
summary_frame.pack()

tk.Button(summary_frame, text="Financial Summary", command=financial_summary).grid(row=0, column=0, padx=5)
tk.Button(summary_frame, text="Expense Breakdown", command=category_breakdown).grid(row=0, column=1, padx=5)
tk.Button(summary_frame, text="Plot Income vs Expenses", command=plot_summary).grid(row=0, column=2, padx=5)
tk.Button(summary_frame, text="Plot Expenses by Category", command=plot_category_breakdown).grid(row=0, column=3, padx=5)

tk.Label(summary_frame, text="Filter Start Date:").grid(row=1, column=0)
start_entry = tk.Entry(summary_frame)
start_entry.grid(row=1, column=1)
tk.Label(summary_frame, text="End Date:").grid(row=1, column=2)
end_entry = tk.Entry(summary_frame)
end_entry.grid(row=1, column=3)
tk.Button(summary_frame, text="Filter", command=filter_date_range).grid(row=1, column=4, padx=5)

# ---------------- Initialize ---------------- #
init_db()
process_recurring()
update_table()
check_budget_alerts()

root.mainloop()

