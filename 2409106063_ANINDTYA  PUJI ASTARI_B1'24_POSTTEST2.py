#Masukkan Nama
nama = input("Masukkan Nama : ")

#Masukkan Gender
gender = input("Masukkan Jenis Kelamin (LAKI LAKI/PEREMPUAN): ")

#Masukkan Tinggi Badan
tinggibadan = float(input("Masukkan Tinggi Badan (dalam satuan Meter, Contoh: 173 CM = 1.73) : "))

#Masukkan Kewarganegaraan
kewarganegaraan_input = input("Masukkan Kewarganegaraan (Menggunakan huruf KAPITAL) :  ")
if kewarganegaraan_input == "INDONESIA" :
    kewarganegaraan = True
if kewarganegaraan_input != "INDONESIA" :
    kewarganegaraan = False

#Masukkan Umur
umur_input = int(input("Masukkan Umur :"))
if umur_input >= 17 :
    umur = True
if umur_input < 17 :
    umur = False

if kewarganegaraan_input == "INDONESIA" and umur_input >= 17 :
    print ("Hai " and nama ,", kamu bisa mengikuti pemilu")
else :
    print ("Hai " and nama ,", kamu tidak bisa mengikuti pemilu" )

#Total Variabel
Umur = umur_input 
TinggiBadan = tinggibadan
(Totalvariabel) = umur_input + TinggiBadan
print("Total Variabel :")
print(float(Totalvariabel))

if  (umur_input >= 17) and (kewarganegaraan_input == "INDONESIA"):
    print("=============================================")
    print("                  Biodata                    ")
    print("=============================================")
    print(f"Nama            : {nama}                    ")
    print(f"Jenis Kelamin   : {gender}                  ")
    print(f"Tinggi Badan    : {tinggibadan}             ")
    print(f"Kewarganegaraan : {kewarganegaraan_input}   ")
    print(f"Umur            : {umur_input}              ")
    print(f"Total Variabel  : {Totalvariabel}           ")
    print(f"Hai {nama}, kamu bisa mengikuti pemilu      ")
    print("=============================================")
else:
    print("=============================================")
    print("                  Biodata                    ")
    print("=============================================")
    print(f"Nama            : {nama}                    ")
    print(f"Jenis Kelamin   : {gender}                  ")
    print(f"Tinggi Badan    : {tinggibadan}             ")
    print(f"Kewarganegaraan : {kewarganegaraan_input}   ")
    print(f"Umur            : {umur_input}              ")
    print(f"Total Variabel  : {Totalvariabel}           ")
    print(f"Hai {nama}, kamu tidak bisa mengikuti pemilu")
    print("=============================================")