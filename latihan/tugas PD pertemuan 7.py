def hitung_diskon(total_bayar):
    diskon_persen = 5
    diskon = (diskon_persen / 100) * total_bayar
    return diskon

def main():
    # Informasi Toko Buku
    print("====================================================")
    print("         Toko Buku Cerdas Selalu                    ")
    print("         Jln. Pinang Sebatang                       ")
    print("====================================================")

    # List Buku
    print("                 List Buku                          ")
    print("====================================================")
    print("kode | Judul Buku        | Harga")
    print("DP   | Dasar Pemrograman | Rp. 150.000")
    print("VB   | Visual Basic      | Rp. 160.000")
    print("WP   | Web Programming   | Rp. 200.000")
    print("====================================================")

    # Input jumlah beli
    jumlah_beli = int(input("Jumlah Beli: "))

    # Inisialisasi variabel total_bayar
    total_bayar = 0

    # Inisialisasi dictionary untuk menyimpan informasi pembelian
    resi_pembelian = []

    # Loop untuk memproses pembelian
    for i in range(1, jumlah_beli + 1):
        print(f"\nBeli ke - {i}")
        kode_buku = input("Masukkan Kode buku [DP/VB/WP]: ")
        jumlah_beli_buku = int(input("Masukkan Jumlah beli: "))

        # Hitung total harga
        if kode_buku == "DP" or kode_buku == "dp":
            judul_buku = "Dasar Pemrograman"
            harga = 150000
        elif kode_buku == "VB" or kode_buku == "vb":
            judul_buku = "Visual Basic"
            harga = 160000
        elif kode_buku == "WP" or kode_buku == "wp":
            judul_buku = "Web Programming"
            harga = 200000
        else:
            print("Kode buku tidak valid. Pembelian dibatalkan.")
            return

        total_harga = jumlah_beli_buku * harga
        total_bayar += total_harga

        # Menambah informasi pembelian ke dalam dictionary
        resi_pembelian.append({
            "judul_buku": judul_buku,
            "jumlah_beli": jumlah_beli_buku,
            "harga_satuan": harga,
            "total_harga": total_harga
        })

        # Output transaksi
        print(f"\nNo.  Judul Buku           Banyak  Harga   Total")
        print(f"{i:2d}.  {judul_buku}{' '*(20-len(judul_buku))} {jumlah_beli_buku:5d}  {harga:6,.0f} {total_harga:8,.0f}")

    # Input uang bayar
    uang_bayar = int(input("\nUang Bayar Rp. "))

    # Hitung diskon
    diskon = hitung_diskon(total_bayar)

    # Hitung total bayar setelah diskon
    total_bayar_setelah_diskon = total_bayar - diskon

    # Hitung kembalian
    kembalian = uang_bayar - total_bayar_setelah_diskon

    # Output hasil akhir
    print("\n====================================================")
    print("              Toko Buku Cerdas Selalu                 ")
    print("                Jln. Pinang Sebatang                  ")
    print("======================================================   ")
    print("No.  Judul Buku           Banyak  Harga   Total")
    for idx, pembelian in enumerate(resi_pembelian, start=1):
        print(f"{idx:2d}.  {pembelian['judul_buku']}{' '*(20-len(pembelian['judul_buku']))} {pembelian['jumlah_beli']:5d}  {pembelian['harga_satuan']:6,.0f} {pembelian['total_harga']:8,.0f}")

    print(f"\nJumlah Bayar Rp. {total_bayar:,.0f}")
    print(f"Diskon 5% Rp. {diskon:,.0f}")
    print(f"Total Bayar Rp. {total_bayar_setelah_diskon:,.0f}")
    print(f"Uang Bayar Rp. {uang_bayar:,.0f}")
    print(f"Kembalian Rp. {kembalian:,.0f}")

if __name__ == "__main__":
    main()
