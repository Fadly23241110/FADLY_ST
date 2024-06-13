# latihan membuat percabangan
print("silahkan masukkan operasi yang diinginkan:")
print("1 -operasi penjumlahan")
print("2 -operasi pengurangan")
pilihan = int(input("Masukkan pilihan anda: "))

if pilihan == 1:
    print("\n ini operasi penjumlahan")
    bil1 = int(input("masukkan bilangan pertama: "))
    bil2 = int(input("masukkan bilangan kedua: "))
    hasil = bil1 + bil2
    print("hasil adalah: ",hasil)
elif pilihan == 2:
    print("\n ini operasi pengurangan")
    bil1 = int(input("Masukkan bilangan pertama: "))
    bil2 = int(input("Masukkan bilangan kedua: "))
    hasil = bil1 - bil2
    print("Hasil adalah:", hasil)
else:
    print("\nangka yang anda pillih tidak ada\npilih angka 1 atau 2")
