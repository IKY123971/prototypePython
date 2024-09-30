# Input
pembeli = input("Input Nama Pembeli : ")
no_hp = input("Input No. Handphone : ")
jurusan = input("Input Jurusan [SBY/BL/LMP] : ")

# Proses
if jurusan == "SBY":
    namajurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL":
    namajurusan = "Bali"
    harga = 350000
else:
    namajurusan = "Lampung"
    harga = 500000

# Input Jumlah Beli
jumlah = int(input("Masukkan Jumlah Beli : "))

# Proses potongan
if jumlah >= 3:
    potongan = (jumlah * harga) * 0.1
else:
    potongan = 0

# Hitung total setelah potongan
total = (jumlah * harga) - potongan

# Cetak Hasil
print("------------------------------------")
print(" PENJUALAN TIKET BUS")
print(" XYZ")
print("------------------------------------")
print("Nama Pembeli : " + pembeli)
print("No. Handphone : " + no_hp)
print("Kode Jurusan yang dipilih : " + jurusan)
print("Nama Kota Tujuan : " + namajurusan)
print("Harga : ", harga)
print("Jumlah Beli : ", jumlah)
print("------------------------------------")
print("Potongan yang didapat : ", potongan)
print("Total Bayar : ", total)

ubay = int(input("Masukkan Uang Bayar : "))
uangkembali = ubay - total
print("Uang Kembali : ", uangkembali)
