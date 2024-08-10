import sqlite3

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS calibration_files (
                        id INTEGER PRIMARY KEY,
                        filename TEXT,
                        key TEXT,
                        value TEXT
                    )''')
    conn.commit()
    return conn

def store_cf_data(conn, cf_data):
    cursor = conn.cursor()
    for filename, data in cf_data.items():
        for key, value in data.items():
            cursor.execute('''INSERT INTO calibration_files (filename, key, value)
                              VALUES (?, ?, ?)''', (filename, key, value))
    conn.commit()

def query_cf_data(conn, key):
    cursor = conn.cursor()
    cursor.execute("SELECT filename, value FROM calibration_files WHERE key=?", (key,))
    return cursor.fetchall()
