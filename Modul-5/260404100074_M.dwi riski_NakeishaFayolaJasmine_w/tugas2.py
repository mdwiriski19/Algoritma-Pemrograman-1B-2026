def anagram(kata1, kata2):
    if sorted(kata1.lower()) == sorted(kata2.lower()):
        return True
    else:
        return False

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

hasil = anagram(kata1, kata2)

if hasil:
    print("Kedua kata merupakan anagram!")
else:
    print("Kedua kata bukan anagram!")