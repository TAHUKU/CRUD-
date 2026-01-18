from database.db import koneksi

class CRUD:

    # ================= CREATE =================
    def create(self, nama, umur, email, no_hp):
        conn = koneksi()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (nama, umur, email, no_hp) VALUES (?, ?, ?, ?)",
            (nama, umur, email, no_hp)
        )

        conn.commit()
        conn.close()

    # ================= READ =================
    def Read(self):
        conn = koneksi()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        conn.close()
        return data

    # ================= UPDATE =================
    def update(self, userid, nama, umur, email, no_hp):
        conn = koneksi()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET nama=?, umur=?, email=?, no_hp=? WHERE id=?",
            (nama, umur, email, no_hp, userid)  # ✔ urutan benar
        )

        conn.commit()
        conn.close()

    # ================= DELETE =================
    def dell(self, userId):
        conn = koneksi()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM users WHERE id=?",
            (userId,)
        )

        conn.commit()
        conn.close()

    # ================= SEARCH =================
    def cari(self, userID):
        conn = koneksi()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE id=?",
            (userID,)
        )

        data = cursor.fetchone()  # ✔ ambil 1 data
        conn.close()
        return data
