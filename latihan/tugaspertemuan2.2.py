jumlah_kucing = int(input("masukan jumlah anak kucing: "))
while jumlah_kucing > 0:
    if jumlah_kucing == 1:
        print(f"{jumlah_kucing} kucing kecil, meong-meong, mati satu, tinggal kucing indah")
    else:
        print(f"{jumlah_kucing} kucing kecil, meong-meong, mati satu, tinggal {jumlah_kucing-1} kucing")
    jumlah_kucing -= 1
