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
                  company TEXT,
                  image TEXT)''')
    conn.commit()
    conn.close()


def save_business_card(info: Dict[str, str]):
    print("saving...")
    conn = sqlite3.connect('business_cards.db')
    c = conn.cursor()
    c.execute('''INSERT INTO business_cards (name, title, phone, email, address, company, image)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (info['name'], info['title'], info['phone'], info['email'], info['address'], info['company'], info['image']))
    conn.commit()
    conn.close()


def get_all_business_cards():
    conn = sqlite3.connect('business_cards.db')
    c = conn.cursor()
    c.execute('SELECT * FROM business_cards')
    cards = c.fetchall()
    conn.close()
    return cards


def update_business_card(card_id: int, info: Dict[str, str]):
    print("updating...")
    conn = sqlite3.connect('business_cards.db')
    c = conn.cursor()
    c.execute('''UPDATE business_cards
                 SET name = ?, title = ?, phone = ?, email = ?, address = ?, company = ?, image = ?
                 WHERE id = ?''',
              (info['name'], info['title'], info['phone'], info['email'], info['address'], info['company'], info['image'], card_id))
    conn.commit()
    conn.close()


def delete_business_card(card_id: int):
    print("deleting...")
    conn = sqlite3.connect('business_cards.db')
    c = conn.cursor()
    c.execute('DELETE FROM business_cards WHERE id = ?', (card_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    save_business_card(
        {
            "name": "김 나 연",
            "title": "Product Manager",
            "phone": "NULL",
            "email": "hello@reallygreatsite.com",
            "address": "123 Anywhere St., Any City, ST 12345",
            "company": "larana",
            "image": "base64imagestring"  # base64 인코딩된 이미지 데이터
        }
    )
    print(get_all_business_cards())
