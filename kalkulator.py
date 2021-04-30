def tambah(x,y):
    return x+y
def kurang(x,y):
    return x-y
def bagi(x,y):
    return x//y
def pangkat(x,y):
    return x*y

print("Pilih Operasi: ")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Pembagian")
print("4.Perpangkatan")

while True :
    pilihan = input("Masukkan Pilihan 1/2/3/4: ")

    if pilihan in ("1", "2", "3", "4"):
        nom1 = int(input("Masukkan Angka Pertama:"))
        nom2 = int(input("Masukkan Angka Kedua: "))

        if pilihan == "1":
           print(nom1, "+", nom2, "=", tambah(nom1, nom2))
        elif pilihan == "2":
            print(nom1, "-", nom2, "=", kurang(nom1,nom2))
        elif pilihan == "3":
            print(nom1, ":", nom2, "=", bagi(nom1,nom2))
        elif pilihan == "4":
            print(nom1, "^2", nom2, "=", pangkat(nom1,nom2))
        break
    else:
        print("Input yang dimasukkan tidak valid")
