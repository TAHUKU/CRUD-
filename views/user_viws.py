from controller.user_controler import UserController
import os

controller = UserController()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nTekan ENTER untuk melanjutkan...")

def menu():
    print("=== MENU USER ===")
    print("1. Tambah User")
    print("2. Lihat User")
    print("3. Edit User")
    print("4. Hapus User")
    print("5. Cari ID")
    print("6. Keluar")

while True:
    clear()
    menu()
    pilihan = input("Pilih: ")

    # ================= TAMBAH USER =================
    if pilihan == "1":
        clear()
        nama = input("Masukkan nama: ")

        try:
            umur = int(input("Masukkan umur: "))
            no_hp = int(input("Masukkan nomor HP: "))
        except ValueError:
            print("❌ Umur dan nomor HP harus angka")
            pause()
            continue

        email = input("Masukkan email: ")
        controller.tambah(nama, umur, email, no_hp)

        print("✅ User berhasil ditambahkan")
        pause()

    # ================= LIHAT USER =================
    elif pilihan == "2":
        clear()
        users = controller.look()

        if users:
            print("ID | Nama | Umur | Email | No HP")
            print("-" * 45)
            for u in users:
                print(f"{u[0]} | {u[1]} | {u[2]} | {u[3]} | {u[4]}")
        else:
            print("❌ Data kosong")

        pause()

    # ================= EDIT USER =================
    elif pilihan == "3":
        clear()
        try:
            id = int(input("ID User: "))
            if not controller.out(id):
                print("❌ ID tidak ditemukan")
                pause()
                continue

            nama = input("Nama baru: ")
            umur = int(input("Umur baru: "))
            email = input("Email baru: ")
            no_hp = int(input("Nomor HP baru: "))

            controller.edit(id, nama, umur, email, no_hp)
            print("✅ Data berhasil diupdate")

        except ValueError:
            print("❌ ID, umur, dan no HP harus angka")

        pause()

    # ================= HAPUS USER =================
    elif pilihan == "4":
        clear()
        try:
            id = int(input("ID User: "))
            if not controller.out(id):
                print("❌ ID tidak ditemukan")
                pause()
                continue

            controller.hapus(id)
            print("✅ User berhasil dihapus")

        except ValueError:
            print("❌ ID harus angka")

        pause()

    # ================= CARI USER =================
    elif pilihan == "5":
        clear()
        try:
            id = int(input("Masukkan ID yang dicari: "))
            if not controller.out(id):
                print("❌ ID tidak ditemukan")
                pause()
                continue

            for u in controller.look():
                if u[0] == id:
                    print("ID | Nama | Umur | Email | No HP")
                    print("-" * 45)
                    print(f"{u[0]} | {u[1]} | {u[2]} | {u[3]} | {u[4]}")
                    break

        except ValueError:
            print("❌ ID harus angka")

        pause()

    # ================= KELUAR =================
    elif pilihan == "6":
        clear()
        print("👋 Program berhenti")
        break

    else:
        print("❌ Pilihan tidak valid")
        pause()
