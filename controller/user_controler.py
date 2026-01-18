from models.user_model import CRUD

class UserController:
    def __init__(self):
        self.model = CRUD()

    # ================= CEK ID =================
    def out(self, user_id):
        users = self.model.Read()
        return any(u[0] == user_id for u in users)

    # ================= CREATE =================
    def tambah(self, nama, umur, email, no_hp):
        self.model.create(nama, umur, email, no_hp)

    # ================= READ =================
    def look(self):
        return self.model.Read()

    # ================= UPDATE =================
    def edit(self, user_id, nama, umur, email, no_hp):
        if not self.out(user_id):
            return False

        self.model.update(user_id, nama, umur, email, no_hp)
        return True

    # ================= DELETE =================
    def hapus(self, user_id):
        if not self.out(user_id):
            return False

        self.model.dell(user_id)
        return True

    # ================= SEARCH =================
    def search(self, user_id):
        if not self.out(user_id):
            return None

        return self.model.cari(user_id)
