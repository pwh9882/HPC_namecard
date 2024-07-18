import sqlite3
from typing import Dict


def init_db():
    conn = sqlite3.connect('business_cards.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS business_cards
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  title TEXT,
                  phone TEXT,
                  email TEXT,
                  address TEXT,
                  company TEXT)''')
    conn.commit()
    conn.close()


def save_business_card(info: Dict[str, str]):
    conn = sqlite3.connect('business_cards.db')
    c = conn.cursor()
    c.execute('''INSERT INTO business_cards (name, title, phone, email, address, company)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (info['name'], info['title'], info['phone'], info['email'], info['address'], info['company']))
    conn.commit()
    conn.close()


def get_all_business_cards():
    conn = sqlite3.connect('business_cards.db')
    c = conn.cursor()
    c.execute('SELECT * FROM business_cards')
    cards = c.fetchall()
    conn.close()
    return cards
