from database.db import koneksi

def init_db():
    conn = koneksi()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            umur INTEGER NOT NULL,
            email TEXT NOT NULL,
            no_hp INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("Tabel users berhasil dibuat")

if __name__ == "__main__":
    init_db()

#membuat tabel database