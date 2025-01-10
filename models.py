import sqlite3

def init_db():
    conn = sqlite3.connect('banking_system.db')
    c = conn.cursor()

    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    account_number TEXT UNIQUE NOT NULL,
                    dob TEXT NOT NULL,
                    city TEXT NOT NULL,
                    password TEXT NOT NULL,
                    balance REAL NOT NULL CHECK (balance >= 2000),
                    contact_number TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL,
                    active INTEGER DEFAULT 1
                 )''')
    
    # Create transaction table
    c.execute('''CREATE TABLE IF NOT EXISTS transaction (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_number TEXT NOT NULL,
                    date TEXT NOT NULL,
                    type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    balance_after REAL NOT NULL,
                    FOREIGN KEY (account_number) REFERENCES users (account_number)
                 )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
