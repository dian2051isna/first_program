# 

bilangan = int(input("Masukkan bilangan bulat: "))
kategori = ""

if bilangan % 2 == 0:
    pesan = "Bilangan tersebut adalah bilangan genap"
else:
    pesan = "Bilangan tersebut adalah bilangan ganjil"

if bilangan < 10:
    kategori = "dan termasuk dalam nilai kecil"
elif 10 <= bilangan <= 50:
    kategori = "dan termasuk dalam nilai sedang"
elif bilangan > 50:
    kategori = "dan termasuk dalam nilai besar"

pesan = pesan + " " + kategori
print(pesan)