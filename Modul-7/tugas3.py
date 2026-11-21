
undangan = set()
webinar_a = set()
webinar_b = set()

print("=== DATA UNDANGAN ===")
while True:
    nama = input("Nama undangan (ketik selesai): ")

    if nama.lower() == "selesai":
        break

    undangan.add(nama)

print("\n=== PESERTA WEBINAR A ===")
while True:
    nama = input("Nama peserta (ketik selesai): ")

    if nama.lower() == "selesai":
        break

    webinar_a.add(nama)

print("\n=== PESERTA WEBINAR B ===")
while True:
    nama = input("Nama peserta (ketik selesai): ")

    if nama.lower() == "selesai":
        break

    webinar_b.add(nama)

print("\n=== HASIL WEBINAR ===")


semua_peserta = webinar_a | webinar_b
print("Semua peserta:", semua_peserta)


kedua_webinar = webinar_a & webinar_b
print("Hadir di kedua webinar:", kedua_webinar)


satu_webinar = webinar_a ^ webinar_b
print("Hadir di salah satu webinar:", satu_webinar)


tidak_hadir = undangan - semua_peserta
print("Tidak hadir:", tidak_hadir)
