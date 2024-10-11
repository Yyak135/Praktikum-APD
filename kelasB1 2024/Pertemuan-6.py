data_mhs = {
    "nama" : "ucup",
    "nim" : 1 ,
    "matkul" : ["APD", "kalkulus", "jarkom"],
    "nama" : "michael",
    "dosen" : {
        "nama" : "pak awang",
        "matkul" : "apd"
    }
}

print(data_mhs["dosen"], ["nama"])

data_mhs['alamat'] = "samarinda"
data_mhs['alamat'] = "tenggarong"
data_mhs.update({"alamat" : "samarinda"})
data_mhs.update({"alamat" : "tenggarong"})

del data_mhs["nim"]

cache = data_mhs.pop("nim")

print(data_mhs, "Dictionary")
print(cache, "cache")

data_mhs["id"] = cache

for data in data_mhs :
    print(data)


for key_data, value_data in data_mhs.items() :
    print(f"Key : {key_data}\nValue : {value_data}\n")


print(data_mhs['nama'])
print(data_mhs['nim'])

print(data_mhs.get['mapel', 'gak ada'])

key = "apel", "jeruk", "mangga", "semangka", "anggur"
value = 1, 5, 9
buah = dict.fromkeys(key, value)
print(buah)

for value in data_mhs.values() :
    print(value)

Nilai = {
    "matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "kimia" : 20,
}


data_mhs = [
    {
     "nama" : "ucup",
     "role" : "admin" 
    },

    {
     "nama" : "michael"
     "role" : "user"
    }
]

print(data_mhs[0]['nama'])
print(data_mhs[1]['nama'])

data_mhs2 = [
    ["ucup", "admin"],
    ["michael", "user"]
]

print(data_mhs[0][[1]])
