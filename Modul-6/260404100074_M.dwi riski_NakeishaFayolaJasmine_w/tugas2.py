
asisten_awal = []

while True:
    nama = input("Masukkan nama asisten awal (cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)

tambahan = input("Masukkan nama asisten tambahan: ")

asisten_akhir = asisten_awal + (tambahan,)

print("\nDaftar asisten akhir:", asisten_akhir)

hari = []

while True:
    nama_hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)

hari = tuple(hari)

pengecualian_asisten = input("\nNama asisten yang dikecualikan: ")
pengecualian_hari = input("Hari yang dikecualikan: ")

print("\nJadwal Shift:")

for asisten in asisten_akhir:
    for nama_hari in hari:

        if asisten == pengecualian_asisten and nama_hari == pengecualian_hari:
            continue

        print(asisten, "-", nama_hari)
