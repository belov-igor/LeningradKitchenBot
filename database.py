# -*- coding: utf-8 -*-
import sqlite3 as sq

db = sq.connect('lk.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER, "
                "tg_name TEXT, "
                "user_name TEXT, "
                "cart_id TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "type TEXT, "
                "name TEXT, "
                "description TEXT, "
                "price TEXT, "
                "photo TEXT)")
    db.commit()


async def cmd_start_db(user_id):
    user = cur.execute(f"SELECT * FROM accounts WHERE tg_id == {user_id}").fetchone()
    if not user:
        cur.execute(f"INSERT INTO accounts (tg_id) VALUES ({user_id})")
        db.commit()


async def add_item(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO items (type, name, description, price, photo, brand) VALUES (?, ?, ?, ?, ?)",
                    (data['type'], data['name'], data['description'], data['price'], data['photo']))
        db.commit()

