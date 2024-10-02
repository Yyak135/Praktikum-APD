import os 
from time import sleep

print("Silahkan Login terlebih dahulu")

kesempatan = 3
while kesempatan > 0 :
    username = input("Masukkan Username : ")
    nim = input("Masukkan Password : ")

    if username == "tya" and nim == "063" :
        print("Berhasil Login")
        break    
    else :     
        print("Username atau Password salah!")
        kesempatan -= 1
        print(f"Kesempatan anda login tersisa {kesempatan} kali\n")
    if kesempatan == 0 :
        print("Kesempatan Login Anda Habis\n\nPROGRAM BERHENTI")
        sleep(5)
        os.system("cls")
        exit()

while True :
    print("\n*NOTES : PROGRAM INI HANYA BISA MENGHITUNG ANGKA DENGAN SATUAN YANG SAMA (jika satuan belum sama, maka anda harus mengkonversikannya secara manual)")
    print("============================================================")
    print("   Menu Program Menghitung Luas dan Keliling Bangun Datar   ")
    print("============================================================")
    print(" 1. Lingkaran\n 2. Trapesium\n 3. Segitiga\n 4. Keluar dari Program")
    print("============================================================")

    menu = float(input("Masukkan Nomor Pilihan Menu : "))
    phi = 3.14

    if menu == 1 :
        print("\nMenu 1 :\n 1.Luas Lingkaran\n 2.Keliling Lingkaran")
        pilihan = float(input("Masukkan nomor pilihan Anda : "))
        if pilihan == 1 :
            r = float(input("Masukkan jari-jari lingkaran : "))
            luas = phi * (r * r)
            print(f"Luas Lingkaran : {luas} ")
            ulang = input("\nPilih menu lagi?(ga/iya) : ")
            if ulang == "ga" :
                print("ANDA KELUAR PROGRAM")
                print("============================================================")
                break
            elif ulang == "iya" :
                print("============================================================\n")
                continue
            else :
                print("INVALID\n!!!!PROGRAM ERROR!!!!\nPROGRAM BERHENTI")
                sleep(5)
                os.system("cls")
                exit()
        elif pilihan == 2 : 
            r = float(input("Masukkan jari-jari lingkaran : "))
            keliling = 2 * phi * r
            print(f"Keliling Lingkaran : {keliling} ")
            ulang = input("\nPilih menu lagi?(ga/iya) : ")
            if ulang == "ga" :
                print("ANDA KELUAR PROGRAM")
                print("============================================================")
                break
            elif ulang == "iya" :
                print("============================================================\n")
                continue
            else :
                print("INVALID\n!!!!PROGRAM ERROR!!!!\nPROGRAM BERHENTI")
                sleep(5)
                os.system("cls")
                exit()
    elif menu == 2 :
        print("\nMenu 2 :\n 1.Luas Trapesium\n 2.Keliling Trapesium")
        pilihan = float(input("Masukkan nomor pilihan Anda : "))
        if pilihan == 1 :
            sisiA = float(input("Masukkan sisiA Trapesium : "))
            sisiB = float(input("Masukkan sisiB Trapesium : "))
            tinggi = float(input("Masukkan tinggi Trapesium : "))
            luas = 1/2 * (sisiA + sisiB) * tinggi
            print(f"Luas Trapesium : {luas} ")
            ulang = input("\nPilih menu lagi?(ga/iya) : ")
            if ulang == "ga" :
                print("ANDA KELUAR PROGRAM")
                print("============================================================")
                break
            elif ulang == "iya" :
                print("============================================================\n")
                continue
            else :
                print("INVALID\n!!!!PROGRAM ERROR!!!!\nPROGRAM BERHENTI")
                sleep(5)
                os.system("cls")
                exit()
        elif pilihan == 2 :
            sisiA = float(input("Masukkan sisiA Trapesium : "))
            sisiB = float(input("Masukkan sisiB Trapesium : "))
            sisiC = float(input("Masukkan sisiC Trapesium : "))
            sisiD = float(input("Masukkan sisiD Trapesium : "))
            keliling = sisiA + sisiB + sisiC + sisiD
            print(f"Keliling Trapesium : {keliling} ")
            ulang = input("\nPilih menu lagi?(ga/iya) : ")
            if ulang == "ga" :
                print("ANDA KELUAR PROGRAM")
                print("============================================================")
                break
            elif ulang == "iya" :
                print("============================================================\n")
                continue
            else :
                print("INVALID\n!!!!PROGRAM ERROR!!!!\nPROGRAM BERHENTI")
                sleep(5)
                os.system("cls")
                exit()
    elif menu == 3 :
        print("\nMenu 3 :\n 1.Luas Segitiga\n 2.Keliling Segitiga")
        pilihan = float(input("Masukkan nomor pilihan Anda : "))
        if pilihan == 1 :
            alas = float(input("Masukkan alas Segitiga : "))
            tinggi = float(input("Masukkan tinggi Segitiga : "))
            luas = 1/2 * alas * tinggi
            print(f"Luas Segitiga : {luas} ")
            ulang = input("\nPilih menu lagi?(ga/iya) : ")
            if ulang == "ga" :
                print("ANDA KELUAR PROGRAM")
                print("============================================================")
                break
            elif ulang == "iya" :
                print("============================================================\n")
                continue
            else :
                print("INVALID\n!!!!PROGRAM ERROR!!!!\nPROGRAM BERHENTI")
                sleep(5)
                os.system("cls")
                exit()
        elif pilihan == 2 :
            sisiA = float(input("Masukkan sisiA Segitiga : "))
            sisiB = float(input("Masukkan sisiB Segitiga : "))
            sisiC = float(input("Masukkan sisiC Segitiga : "))
            keliling = sisiA + sisiB + sisiC
            print(f"Keliling Segitiga : {keliling} ")
            ulang = input("\nPilih menu lagi?(ga/iya) : ")
            if ulang == "ga" :
                print("ANDA KELUAR PROGRAM")
                print("============================================================")
                break
            elif ulang == "iya" :
                print("============================================================\n")
                continue
            else :
                print("INVALID\n!!!!PROGRAM ERROR!!!!\nPROGRAM BERHENTI")
                sleep(5)
                os.system("cls")
                exit()

    else :
        print("\nINVALID\n!!!!!PROGRAM ERROR!!!!\nPROGRAM BERHENTI")
        sleep(5)
        os.system("cls")
        exit()
       


sleep(5)
os.system("cls") 

