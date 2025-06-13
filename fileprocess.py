# file = open("nama-file.txt", "r")

# print(file.read())
## untuk membaca file

# file = open("nama-file.txt", "w")
# file.write("Ini adalah contoh penulisan ke dalam file.")
# file.close()
## untuk menulis ke dalam file

file = open("nama-file.txt", "a") #"a" untuk append
file.write("\nIni adalah tambahan teks ke dalam file.")
file.close()
## untuk menambahkan teks ke dalam file. \n untuk enter/line baru