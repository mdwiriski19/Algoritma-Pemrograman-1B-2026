
data_mahasiswa = []

jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0

for i in range(10):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Masukkan nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    data_mahasiswa.append({
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": nilai_akhir,
        "kategori": kategori
    })

    total_nilai += nilai_akhir

print("\n===== DATA NILAI MAHASISWA =====")

for m in data_mahasiswa:
    print(
        m["nama"],
        "| Tugas:", m["tugas"],
        "| UTS:", m["uts"],
        "| UAS:", m["uas"],
        "| Nilai akhir:", round(m["akhir"], 2),  
        "| Kategori:", m["kategori"]
    )

nilai_tertinggi = data_mahasiswa[0]
nilai_terendah = data_mahasiswa[0]

for m in data_mahasiswa:
    if m["akhir"] > nilai_tertinggi["akhir"]:
        nilai_tertinggi = m

    if m["akhir"] < nilai_terendah["akhir"]:
        nilai_terendah = m

rata_rata = total_nilai / 10

print("\n===== REKAP NILAI =====")
print("Jumlah kategori A:", jumlah_A)
print("Jumlah kategori B:", jumlah_B)
print("Jumlah kategori C:", jumlah_C)
print("Jumlah kategori D:", jumlah_D)
print("Jumlah kategori E:", jumlah_E)

print("Nilai tertinggi:", round(nilai_tertinggi["akhir"], 2),
      "-", nilai_tertinggi["nama"])
print("Nilai terendah:", round(nilai_terendah["akhir"], 2),
      "-", nilai_terendah["nama"])
print("Rata-rata kelas:", round(rata_rata, 2))
