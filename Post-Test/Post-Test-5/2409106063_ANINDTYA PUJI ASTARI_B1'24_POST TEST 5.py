import os
from time import sleep
os.system('cls || clear')


pengguna = [["tya", "063", "admin"]]


KaryaSeni = [
    ["Monalisa", "Leonardo da Vinci", 1503, 100],
    ["Starry Night", "Vincent van Gogh", 1889, 500],
    ["Water Lilies", "Pablo Picasso", 1893, 3000]
]

KonfirmasiLogin = False
User = ""
Role = ""

while True:
    if not KonfirmasiLogin:
        print("\tSistem Manajemen Galeri Seni")
        print("=" * 45)
        print("1. Masuk\n2. Daftar\n0. Keluar")
        pilihan = input("Pilih menu: ")
        os.system('cls || clear')

        
        if pilihan == "1":
            print("\t\tLogin\n", "=" * 35)
            Username = input("Nama Pengguna: ")
            Password = input("Kata Sandi: ")
            
            for user in pengguna:
                if user[0] == Username and user[1] == Password:
                    KonfirmasiLogin = True
                    User = user[0]
                    Role = user[2]
                    print(f"Berhasil Masuk Dengan Role {Role}")
                    input("Tekan Enter untuk melanjutkan...")
                    os.system('cls || clear')
                    break
            
            if not KonfirmasiLogin:
                print("Nama pengguna atau kata sandi anda salah!")
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls || clear')

                
        elif pilihan == "2":
            print("\tMenu Pendaftaran\n", "=" * 35)
            UsernameBaru = input("Nama Pengguna baru: ")
            
            
            UsernameTersedia = False
            for user in pengguna:
                if user[0] == UsernameBaru:
                    UsernameTersedia = True
                    print("Nama pengguna sudah digunakan!")
                    input("Tekan Enter untuk melanjutkan...")
                    os.system('cls || clear')
                    break
            
            if not UsernameTersedia:
                Password_baru = input("Kata Sandi baru: ")
                pengguna.append([UsernameBaru, Password_baru, "pengunjung"])
                print("Pendaftaran berhasil! Anda terdaftar sebagai pengunjung.")
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls || clear')

                
        elif pilihan == "0":
            print("Terima kasih telah Berkunjung!.")
            sleep(5)
            os.system('cls || clear')
            
        else:
            print("Pilihan Tidak Tersedia")
            sleep(5)
            os.system('cls || clear')
            
    else:  
        print(f"\tMenu {Role} Galeri Seni\n", "=" * 45, "\n1. Lihat Koleksi Karya Seni")
        if Role == "admin":
            print("2. Tambah Karya Seni\n3. Perbarui Informasi Karya Seni\n4. Hapus Karya Seni")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":  
            print("\nKoleksi Karya Seni:")
            print(f"{'Judul':<20} {'Seniman':<25} {'Tahun':<10} {'Harga (IDR)':<15}")
            print("=" * 70)
            for karya in KaryaSeni:
                judul, seniman, tahun, harga = karya
                print(f"{judul:<20} {seniman:<25} {tahun:<10} {harga:<15,}")
            input("\nTekan Enter untuk melanjutkan...")
            os.system('cls || clear')

                
        elif pilihan == "2" and Role == "admin":  
            print("\n=== Tambah Karya Seni ===")
            judul = input("Judul karya: ")
            seniman = input("Nama seniman: ")
            tahun = int(input("Tahun pembuatan: "))
            harga = int(input("Harga karya (dalam IDR): "))
            KaryaSeni.append([judul, seniman, tahun, harga])
            print("Karya seni berhasil ditambahkan ke koleksi!")
            input("Tekan Enter untuk melanjutkan...")
            

            
        elif pilihan == "3" and Role == "admin": 
            print("\tPerbarui Karya Seni")
            print("=" * 45, "\nDaftar Karya Seni :")
            for i, karya in enumerate(KaryaSeni, 1):
                print(f"{i}. {karya[0]} oleh {karya[1]}")
            
            index = int(input("\nPilih nomor karya yang akan diperbarui: ")) - 1
            if 0 <= index < len(KaryaSeni):
                judul = input("Judul karya baru (kosongkan jika tidak ingin diubah): ")
                seniman = input("Nama seniman baru (kosongkan jika tidak ingin diubah): ")
                tahun = input("Tahun pembuatan baru (kosongkan jika tidak ingin diubah): ")
                harga = input("Harga baru (kosongkan jika tidak ingin diubah): ")
                
                if judul:
                    KaryaSeni[index][0] = judul
                if seniman:
                    KaryaSeni[index][1] = seniman
                if tahun:
                    KaryaSeni[index][2] = int(tahun)
                if harga:
                    KaryaSeni[index][3] = int(harga)
                print("Informasi karya seni berhasil diperbarui!")
            else:
                print("Nomor karya tidak valid!")
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls || clear')

                
        elif pilihan == "4" and Role == "admin": 
            print("\n=== Hapus Karya Seni ===")
            print("Daftar Karya Seni:")
            for i, karya in enumerate(KaryaSeni, 1):
                print(f"{i}. {karya[0]} oleh {karya[1]}")
            
            index = int(input("\nPilih nomor karya yang akan dihapus: ")) - 1
            if 0 <= index < len(KaryaSeni):
                hapus = KaryaSeni.pop(index)
                print(f"Karya '{hapus[0]}' oleh {hapus[1]} berhasil dihapus dari koleksi!")
            else:
                print("Nomor karya tidak valid!")
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls || clear')

                
        elif pilihan == "0": 
            KonfirmasiLogin = False
            User = ""
            Role = ""
            print("Anda Telah Keluar.")
            sleep(5)
            os.system('cls || clear')
            exit()
            
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")
            os.system('cls || clear')
