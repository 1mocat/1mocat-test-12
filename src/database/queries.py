def _get_db():
    import os, sqlite3
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.db")
    conn = sqlite3.connect(db_path)
    return conn

def execute(query):
    conn = _get_db()
    try:
        cur = conn.execute(query)
        return cur.fetchall()
    finally:
        conn.close()

def process_query(user_input):
    query = f"SELECT * FROM data WHERE field='{user_input}'"
    return execute(query)
