karyawan=input("Nama karyawan : ")
golongan=int(input("Golongan jabatan : "))
pendidikan=input("pendidikan :  ")
jamkerja=float(input("jumlah jam kerja : "))

def hitung_tunjangan_jabatan(golongan):
    if golongan == 1:
        return 0.05 * 300000
    elif golongan == 2:
        return 0.10 * 300000
    elif golongan == 3:
        return 0.15 * 300000
    else:
        return 0 
    
def hitung_tunjangan_pendidikan(pendidikan):
    if pendidikan=="SMA":
        return 0.025 * 300000
    elif pendidikan=="D1":
        return 0.05 * 300000
    elif pendidikan=="D3":
        return 0.20 * 300000
    elif pendidikan=="S1":
        return 0.30 * 300000
    else:
        return 0
    
def hitung_honor_lembur(jamkerja):
    if jamkerja > 8:
        kelebihan_jam = jamkerja - 8
        return kelebihan_jam * 3500
    else:
        return 0
    
tunjangan_jabatan = hitung_tunjangan_jabatan(golongan)
tunjangan_pendidikan = hitung_tunjangan_pendidikan(pendidikan)
honor_lembur = hitung_honor_lembur(jamkerja)

gaji_pokok = 300000
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur


print("------------------------------------")
print("PROGRAM HITUNG GAJI KARYAWAN PT DINGIN DAMAI")
print("------------------------------------")
print("Karyawan yang bernama : "+str(karyawan))
print("Honor yang diterima")
print("Tunjangan jabatan : "+str(golongan))
print("Tunjangan pendidikan : "+str(pendidikan))
print("Jumlah jam kerja : ",+(jamkerja))
print(f"Total gaji karyawan adalah: Rp. {total_gaji:.2f}")
print("------------------------------------")