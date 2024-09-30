print ("        GEROBAK FRIED CHIKEN       ")
print ("-----------------------------------")
print ("kode     jenis potong        harga")
print ("-----------------------------------")
print ("D        dada                RP.2500")
print ("P        paha                Rp.2000")
print ("S        sayap               Rp.1500")
print ("-----------------------------------")

banyak_jenis = int(input("Banyak jenis: "))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []

i = 0
while i < banyak_jenis:
    print("Jenis ke-", i + 1)
    kode_potong.append(input("Kode potong [D/P/S]: "))
    banyak_potong.append(int(input("Banyak potong: ")))

    if kode_potong[i] == "D" or kode_potong[i] == "d":
        jenis_potong.append("dada")
        harga.append(2500)
        jumlah.append(banyak_potong[i] * 2500)

    elif kode_potong[i] == "P" or kode_potong[i] == "p":
        jenis_potong.append("paha")
        harga.append(2000)
        jumlah.append(banyak_potong[i] * 2000)

    elif kode_potong[i] == "S" or kode_potong[i] == "s":
        jenis_potong.append("sayap")
        harga.append(1500)
        jumlah.append(banyak_potong[i] * 1500)

    else:
        jenis_potong.append("kode salah")
        harga.append(0)
        jumlah.append(banyak_potong[i] * 0)
    i = i + 1

# Print
print("                                   ")
print("        GEROBAK FRIED CHIKEN"       )
print("------------------------------------")
print("NO. Jenis    Harga   Banyak  Jumlah")
print("    Potong   Satuan  Beli    Harga")
print("------------------------------------")

jumlah_bayar = 0
a = 0
while a < banyak_jenis:
    jumlah_bayar = jumlah_bayar + jumlah[a]
    print("%i   %s     %s    %i      %i" % (a+1, jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
    a = a + 1

pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("------------------------------------")
print("              Jumlah bayar Rp.",jumlah_bayar)
print("              Pajak 10%    Rp.",pajak)
print("              Total bayar  Rp.",total_bayar)
