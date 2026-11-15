
total_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = float(input("Masukkan jarak tempuh (km): ")) 

    if jarak == 0:
        break  

    if jarak < 0: 
        print("Jarak tidak valid, masukkan ulang!")
        continue  
    
    total_penumpang += 1
    total_jarak += jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if total_penumpang % 5 == 0:
        tarif *= 0.5
        print("Mendapat diskon 50%")

    total_pendapatan += tarif

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print("Tarif: Rp", int(tarif))

if total_penumpang > 0:
    rata_rata = total_jarak / total_penumpang
    print("\nJumlah penumpang:", total_penumpang)
    print("Total pendapatan: Rp", int(total_pendapatan))
    print("Jarak terjauh:", jarak_terjauh, "km")
    print("Rata-rata jarak:", round(rata_rata, 2), "km")
else:
    print("Belum ada penumpang.")

