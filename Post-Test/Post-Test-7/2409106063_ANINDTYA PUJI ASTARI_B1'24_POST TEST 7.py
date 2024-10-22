import os
from time import sleep

os.system('cls || clear')

pengguna = {
    "tya": {"password": "063", "role": "admin"}
}

KaryaSeni = {
    1: {"judul": "Monalisa", "seniman": "Leonardo da Vinci", "tahun": 1503, "harga": 100},
    2: {"judul": "Starry Night", "seniman": "Vincent van Gogh", "tahun": 1889, "harga": 500},
    3: {"judul": "Water Lilies", "seniman": "Pablo Picasso", "tahun": 1893, "harga": 3000}
}

KonfirmasiLogin = False
User = ""
Role = ""

def clear_screen():
    os.system('cls || clear')

def tampilkan_koleksi_karya_seni():
    print("\nKoleksi Karya Seni:")
    print(f"{'Judul':<20} {'Seniman':<25} {'Tahun':<10} {'Harga (USD)':<15}")
    print("=" * 70)
    for karya in KaryaSeni.values():
        print(f"{karya['judul']:<20} {karya['seniman']:<25} {karya['tahun']:<10} {karya['harga']:<15,}")

def daftar_karya_seni():
    print("=" * 45, "\nDaftar Karya Seni :")
    for i, karya in KaryaSeni.items():
        print(f"{i}. {karya['judul']} oleh {karya['seniman']}")

def tambah_karya_seni(judul, seniman, tahun, harga):
    KaryaSeni[len(KaryaSeni) + 1] = {"judul": judul, "seniman": seniman, "tahun": tahun, "harga": harga}
    return "Karya seni berhasil ditambahkan ke koleksi!"

def edit_karya_seni(index, judul='', seniman='', tahun='', harga=''):
    if index in KaryaSeni:
        if judul:
            KaryaSeni[index]["judul"] = judul
        if seniman:
            KaryaSeni[index]["seniman"] = seniman
        if tahun:
            KaryaSeni[index]["tahun"] = int(tahun)
        if harga:
            KaryaSeni[index]["harga"] = int(harga)
        return "Informasi karya seni berhasil diperbarui!"
    else:
        return "Nomor karya tidak valid!"

def hapus_karya_seni():
    index = int(input("\nPilih nomor karya yang akan dihapus: "))
    if index in KaryaSeni:
        hapus = KaryaSeni.pop(index)
        return f"Karya '{hapus['judul']}' oleh {hapus['seniman']} berhasil dihapus dari koleksi!"
    else:
        return "Nomor karya tidak valid!"

def logout():
    global KonfirmasiLogin, User, Role
    KonfirmasiLogin = False
    User = ""
    Role = ""
    print("Anda telah berhasil Logout. Kembali ke menu autentikasi...")

def login():
    global KonfirmasiLogin, User, Role
    print("\t\tLogin\n", "=" * 35)
    Username = input("Nama Pengguna: ")
    Password = input("Kata Sandi: ")

    if Username in pengguna and pengguna[Username]["password"] == Password:
        KonfirmasiLogin = True
        User = Username
        Role = pengguna[Username]["role"]
        print(f"Berhasil Masuk Dengan Role {Role}")
    else:
        print("Nama pengguna atau kata sandi salah!")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()

def register():
    print("\tMenu Pendaftaran\n", "=" * 35)
    UsernameBaru = input("Nama Pengguna baru: ")

    UsernameTersedia = False
    for user in pengguna:
        if UsernameBaru in pengguna:
            UsernameTersedia = True
            print("Nama pengguna sudah digunakan!")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
            break

    if not UsernameTersedia:
        Password_baru = input("Kata Sandi baru: ")
        pengguna[UsernameBaru] = {"password": Password_baru, "role": "pengunjung"}
        print("Pendaftaran berhasil! Anda terdaftar sebagai pengunjung.")
        input("Tekan Enter untuk melanjutkan...")
        clear_screen()


while True:
    if not KonfirmasiLogin:
        print("\tSistem Manajemen Galeri Seni")
        print("=" * 45)
        print("1. Masuk\n2. Daftar\n0. Keluar")
        pilihan = input("Pilih menu: ")
        clear_screen()

        if pilihan == "1":
           login()

        elif pilihan == "2":
            register()

        elif pilihan == "0":
            print("Terima kasih telah Berkunjung!.")
            sleep(5)
            os.system('cls || clear')
            break

        else:
            print("Pilihan Tidak Tersedia")
            sleep(5)
            os.system('cls || clear')

    else:
        print(f"\n\tMenu {Role} Galeri Seni\n", "=" * 45, "\n1. Lihat Koleksi Karya Seni")
        if Role == "admin":
            print("2. Tambah Karya Seni\n3. Perbarui Informasi Karya Seni\n4. Hapus Karya Seni")
        print("5. Logout akun\n0. Keluar Program")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_koleksi_karya_seni()
            input("\nTekan Enter untuk melanjutkan...")
            clear_screen()

        elif pilihan == "2" and Role == "admin":
            print("\n=== Tambah Karya Seni ===")
            judul = input("Judul karya: ")
            seniman = input("Nama seniman: ")
            tahun = int(input("Tahun pembuatan: "))
            harga = int(input("Harga karya (dalam USD): "))
            print(tambah_karya_seni(judul, seniman, tahun, harga))
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()

        elif pilihan == "3" and Role == "admin":
            print("\n\tPerbarui Karya Seni")
            daftar_karya_seni()
            tampilkan_koleksi_karya_seni()
            index = int(input("\nPilih nomor karya yang akan diperbarui: "))
            judul = input("Judul karya baru (kosongkan jika tidak ingin diubah): ")
            seniman = input("Nama seniman baru (kosongkan jika tidak ingin diubah): ")
            tahun = input("Tahun pembuatan baru (kosongkan jika tidak ingin diubah): ")
            harga = input("Harga baru (kosongkan jika tidak ingin diubah): ")
            print(edit_karya_seni(index, judul, seniman, tahun, harga))
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "4" and Role == "admin":
            print("\n=== Hapus Karya Seni ===")
            daftar_karya_seni()
            tampilkan_koleksi_karya_seni()
            hapus_karya_seni() 
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "5":
            logout()
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()

        elif pilihan == "0": 
            KonfirmasiLogin = False
            User = ""
            Role = ""
            print("Anda Telah Keluar Program.")
            sleep(5)
            os.system('cls||clear')
            exit()

        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
