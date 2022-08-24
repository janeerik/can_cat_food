import sqlite3

conn = sqlite3.connect("database.sqlite")

with open("schema.sql") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()
