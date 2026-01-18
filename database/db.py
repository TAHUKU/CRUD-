import sqlite3 #penyimpanan database

def koneksi(): #membuat koneksi ke database
    return sqlite3.connect("hakkul.db") # kembali coneksi dengan nama hakkul.db

