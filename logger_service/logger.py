import sqlite3

def init_db():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS connections
                (pid INT, process TEXT, local_address TEXT,
                remote_address TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def save_log(connection):
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute("INSERT INTO connections VALUES (?, ?, ?, ?, ?)", (
        connection['pid'],
        connection['process'],
        connection['local_address'],
        connection['remote_address'],
        connection['status']
    ))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM connections")
    rows = c.fetchall()
    conn.close()
    return rows