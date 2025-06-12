nama1 = "Budi"
nama2 = 'Nina'
#untuk string menggunakan 'petik 1' atau "petik 2"
#namun bila ingin mencetak petik tersebut digunakan
# "\"\"" untuk mengutip petik dalam kalimat
print(nama1)
print("\"Halo nama saya Budi\"")

nama = 'Budi Arie Setiadi'

print(nama.split(' '))  # Memisahkan string berdasarkan spasi
print(nama.split('i'))  # Memisahkan string berdasarkan huruf 'i'
print(nama.upper())  # Mengubah string menjadi huruf kapital
print(nama.lower())  # Mengubah string menjadi huruf kecil
print(nama[0])  # Mengakses karakter pertama dari string

mangga = 5
apel = 7
pisang = 3
text = nama + " " + "membeli {} buah mangga, {} buah apel, dan {} buah pisang" 
# Menggunakan format string untuk memasukkan variabel ke dalam string

print(text.format(mangga, apel, pisang))  # Output: nama1 membeli 5 buah mangga, 7 buah apel, dan 3 buah pisang
