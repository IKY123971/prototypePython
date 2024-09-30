data_product = {
    1:"Laptop",
    2:"Mouse ",
    3:"Monitor",
    4:"Mouse Pad",
    5:"Charger",
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
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash on Delivery",
    4:"Kartu Kredit",
}
print("------------------------------------------------------------------------------------------")
print("                          List Product Toko MITRA KOMPUTER ID                             ")
print("------------------------------------------------------------------------------------------")
for i in data_product:
    print("Id Product : ", i, "\t Nama Product : ",
          data_product[i], "\t \t Harga Product : ", daftar_harga[i])
pilih_id = int(input("Pilih Id Product : "))
if pilih_id in data_product :
    pilih_beli = input("Ingin Beli ? (Y/N): ")
    if pilih_beli == "y" or pilih_beli=="y":
        nama_penerima    = input("Nama Penerima    : ")
        alamat_penerima  = input("Alamat Penerima  : ")
        telepon          = input("No Hp            : ")
        kurir_pengiriman = input("Kurir Pengiriman : ")
        dict_trx = {
            "Nama Penerima":nama_penerima,
            "Alamat Penerima":alamat_penerima,
            "No Hp":telepon,
            "Kurir Pengiriman":kurir_pengiriman,
            "Product Id":data_product,
        }
    else:
        raise SystemExit ("Transaksi anda dibatalkan")
    if len (dict_trx) > 0 :
        print("-------------------------------------------------------")
        print("                  Metode Pembayaran                    ")
        print("-------------------------------------------------------")
    for i in daftar_metode_pembayaran:
        print("Id : ", i, "\t Metode Pembayaran : ", daftar_metode_pembayaran[i])
    pilih_metode = int(input("Pilih ID Metode Pembayaran : "))
    if pilih_metode in daftar_metode_pembayaran :
        print("Nama Penerima : ", dict_trx["Nama Penerima"])
        print("Alamat Penerima : ", dict_trx["Alamat Penerima"])
        print("No Hp : ", dict_trx["No Hp"])
        print("Kurir Pengeriman : ", dict_trx["Kurir Pengiriman"])
        print("Product : ", data_product[pilih_id])
        print("Harga : ", daftar_harga[pilih_id])
        print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("Apakah Anda Yakin ingin melakukan pembayaran? (Y/N) : ")
        if konfirmasi == "y" or konfirmasi == "Y":
            print("-------------------------------------------------------------------")
            print("Terimakasih!, Pembayaran anda sudah berhasil. Pesanan akan diproses")
            print("-------------------------------------------------------------------")
        else:
            raise SystemExit ("Pembayan anda dibatalkan")
    else:
        print("Id metode pembayaran tidak tersedia")
else:
    print("Id product tidak tersedia")

    #Anggota Kelompok 3
    #Arya Dianda Putra Mahardika
    #Arya Salim
    #Muhammad Alfarizki
    #Muhammad Rangga Maulana
    #Satrio Wicaksono
