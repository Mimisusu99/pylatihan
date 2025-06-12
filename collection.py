# append, insert
# remove, pop, del, clear
# list iteration
# check if an item exists in list
# methods: len, copy, concat (+ dan extend), index, sort, reverse

listExample = [1, 2, 'biji', 3.14, 50]
listExample.insert(2, 'baru')
listExample.append('akhir')
listExample.insert(0, 'awal')
listExample.remove(50)
listExample.pop() # removes the last item
print(listExample) 
listExample.clear() # to clear the list
print(listExample)

# List iteration

contohList = [100, 200, 500, 1000, 2000]
for item in contohList:
    print(item)

len = len(contohList) # Get the length of the list
print("Panjang list:", len)

contohList.sort() 
print(contohList) # Sort the list in ascending order

# Tuple , digunakan untuk data yang tidak berubah
contohTuple = (1, 'es', 3.14, 100, 'fakta')
print(contohTuple)
# contohTuple[0] = 10 # Ini akan menghasilkan error karena tuple tidak bisa diubah

# Dictionary , digunakan untuk data yang berpasangan (key-value)
contohDict = {
    'nama': 'John Roe',
    'umur': 30,
    'kota': 'Jakarta'
}
print(contohDict)

# Set , adalah kumpulan elemen unik yang tidak berurutan
contohSet1 = {1, 2, 3, 4, 5}
contohSet2 = {4, 5, 6, 7, 8}
contohSet3 = contohSet1.union(contohSet2)  # Menggabungkan dua set
contohSet4 = contohSet1.intersection(contohSet2)  # Mencari irisan dua set
contohSet5 = contohSet1.difference(contohSet2)  # Mencari perbedaan antara dua set
contohSet6 = contohSet1.symmetric_difference(contohSet2) # Tidak memunculkan yang ada di keduanya

print(contohSet3)
print(contohSet4)
print(contohSet5)
print(contohSet6)