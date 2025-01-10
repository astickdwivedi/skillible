import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def get_db_connection():
    conn = sqlite3.connect('banking_system.db')
    conn.row_factory = sqlite3.Row
    return conn

def add_user(name, dob, city, password, balance, contact_number, email, address):
    account_number = generate_account_number()
    hashed_password = generate_password_hash(password)
    
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''INSERT INTO users (name, account_number, dob, city, password, balance, contact_number, email, address) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
              (name, account_number, dob, city, hashed_password, balance, contact_number, email, address))
    conn.commit()
    conn.close()
    return account_number

def generate_account_number():
    import random
    return ''.join(random.choices('0123456789', k=10))

def validate_login(account_number, password):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE account_number = ?', (account_number,))
    user = c.fetchone()
    conn.close()
    if user and check_password_hash(user['password'], password):
        return user
    return None

def get_user_details(account_number):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE account_number = ?', (account_number,))
    user = c.fetchone()
    conn.close()
    return user

def record_transaction(account_number, type, amount):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT balance FROM users WHERE account_number = ?', (account_number,))
    balance = c.fetchone()[0]
    
    if type == 'debit' and amount > balance:
        return False
    
    new_balance = balance + amount if type == 'credit' else balance - amount
    c.execute('UPDATE users SET balance = ? WHERE account_number = ?', (new_balance, account_number))
    c.execute('INSERT INTO transaction (account_number, date, type, amount, balance_after) VALUES (?, datetime("now"), ?, ?, ?)', 
              (account_number, type, amount, new_balance))
    conn.commit()
    conn.close()
    return True
