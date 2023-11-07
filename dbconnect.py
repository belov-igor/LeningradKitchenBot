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
                "by_weight INTEGER, "
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
    data = await state.get_data()
    cur.execute("INSERT INTO items (type, name, by_weight, description, price, photo) VALUES (?, ?, ?, ?, ?, ?)",
                (data['type'], data['name'], data['by_weight'], data['description'], data['price'], data['photo']))
    db.commit()


async def get_dishes(dish_type):
    dishes = cur.execute("SELECT * FROM items WHERE type = ?", (dish_type,)).fetchall()
    return dishes
    # return dishes
