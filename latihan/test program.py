data_product = {
    1: "Laptop",
    2: "Mouse",
    3: "Monitor",
    4: "Mouse Pad",
    5: "Charger",
}

daftar_harga = {
    1: 5000000,
    2: 60000,
    3: 1500000,
    4: 50000,
    5: 30000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1: "Transfer Bank",
    2: "Virtual Account",
    3: "Cash on Delivery",
    4: "Kartu Kredit",
}

print("------------------------------------------------------------------------------------------")
print("                          List Product Toko MITRA KOMPUTER ID                             ")
print("------------------------------------------------------------------------------------------")
for i in data_product:
    print("Id Product : ", i, "\t Nama Product : ", data_product[i], "\t \t Harga Product : ", daftar_harga[i])

# Input for multiple items
banyak_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))

# Initialize transaction details
dict_trx = {
    "Nama Penerima": input("Nama Penerima    : "),
    "Alamat Penerima": input("Alamat Penerima  : "),
    "No Hp": input("No Hp            : "),
    "Kurir Pengiriman": input("Kurir Pengiriman : "),
    "Product Id": [],
}

total_harga = 0

for _ in range(banyak_barang):
    pilih_id = int(input("Pilih Id Product : "))
    if pilih_id in data_product:
        dict_trx["Product Id"].append(pilih_id)
        total_harga += daftar_harga[pilih_id]
    else:
        print("Id product tidak tersedia. Transaksi dibatalkan.")
        raise SystemExit("Transaksi anda dibatalkan")

# Display transaction details
print("-------------------------------------------------------")
print("                  Metode Pembayaran                    ")
print("-------------------------------------------------------")

for i in daftar_metode_pembayaran:
    print("Id : ", i, "\t Metode Pembayaran : ", daftar_metode_pembayaran[i])

pilih_metode = int(input("Pilih ID Metode Pembayaran : "))
if pilih_metode in daftar_metode_pembayaran:
    print("Nama Penerima : ", dict_trx["Nama Penerima"])
    print("Alamat Penerima : ", dict_trx["Alamat Penerima"])
    print("No Hp : ", dict_trx["No Hp"])
    print("Kurir Pengeriman : ", dict_trx["Kurir Pengiriman"])

    print("\n---- Detail Pembelian ----")
    for p_id in dict_trx["Product Id"]:
        print("Product : ", data_product[p_id])
        print("Harga : ", daftar_harga[p_id])
        print("--------------------------")

    print("Total Harga : ", total_harga)
    print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])

    konfirmasi = input("Apakah Anda Yakin ingin melakukan pembayaran? (Y/N) : ").lower()
    if konfirmasi == "y":
        print("-------------------------------------------------------------------")
        print("Terimakasih!, Pembayaran anda sudah berhasil. Pesanan akan diproses")
        print("-------------------------------------------------------------------")
    else:
        raise SystemExit("Pembayaran anda dibatalkan")

else:
    print("Id metode pembayaran tidak tersedia")
