# Class
# python adalah bahasa pemrograman yang berorientasi objek, artinya kita dapat membuat kelas dan objek
# hampir semua hal di python adalah objek, termasuk fungsi, kelas, dan modul 
# sebuah kelas adalah cetak biru untuk membuat objek, yang merupakan instansi dari kelas tersebut

class Person:
    nama = "John Doe"

obj = Person()
print(type(obj))  # Output: <class '__main__.Person'>
print(obj.nama)  # Output: John Doe

class Animal:
    spesies = "Dog"

obj2 = Animal()
print(type(obj2))  # Output: <class '__main__.Animal'>
print(obj2.spesies)  # Output: Dog

# __init__() # method adalah konstruktor yang digunakan untuk menginisialisasi atribut objek saat objek dibuat
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

p1 = Car("Toyota", "Corolla")
p2 = Car("Honda", "Civic")

print(p1.brand, p1.model)  # Output: Toyota Corolla
print(p2.brand, p2.model)  # Output: Honda Civic

print(p1.__dict__)  # Output: {'brand': 'Toyota', 'model': 'Corolla'}
print(p2.__dict__)  # Output: {'brand': 'Honda', 'model': 'Civic'}