kode_baju = input ("masukan kode baju [SP/AD]: ")
ukuran = input ('masukan ukuran baju [S/M]: ')
jumlah = int(input ("masukan jumlah beli: "))

if kode_baju == "SP" or kode_baju == "sp" :
    merk = "super dry"
    if ukuran == "S" or ukuran == "s":
        harga = 45000
    elif ukuran == "M" or ukuran == "m":
        harga = 50000
    else:
        harga = 0

elif kode_baju == "AD" or kode_baju == "ad":
    merk = "adidas"
    if ukuran == "S" or ukuran == "s":
        harga = 65000
    elif ukuran == "M" or ukuran == "m":
        harga = 70000
    else: 
        harga = 0

else: 
    merk = "anda salah input merk"
    harga = 0
total = jumlah * harga 


print("----------------------------------")
print ("merk baju : ", (merk))
print ("merk harga baju : Rp.", harga)
print ("total harga yg harus dibayar adalah: Rp.", (total))