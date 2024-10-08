# Input nama, NIM, dan harga gula
nama = input ("Nama Lengkap : ")
nim =  input ("NIM : ")
harga_gula = float(input("Masukkan harga gula: Rp "))

# Persentase diskon
diskon_gulaku = 0.07
diskon_manis_kita = 0.11
diskon_gunung_madu = 0.13

# Menghitung harga setelah diskon
harga_gulaku = harga_gula - (harga_gula * diskon_gulaku)
harga_manis_kita = harga_gula - (harga_gula * diskon_manis_kita)
harga_gunung_madu = harga_gula - (harga_gula * diskon_gunung_madu)

# Menampilkan hasil
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"Harga gula seharga gula: Rp {harga_gula}")
print(f"Jika dia membeli Gulaku ia harus membayar Rp {harga_gulaku} Setelah mendapat diskon 7%")
print(f"Jika dia membeli Manis Kita ia harus membayar Rp {harga_manis_kita} Setelah mendapat diskon 11%")
print(f"Jika dia membeli Gunung Madu ia harus membayar Rp {harga_gunung_madu} Setelah mendapat diskon 13%")