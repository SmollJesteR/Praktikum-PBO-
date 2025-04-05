# MUHAMMAD ROYHAN ALFITRA
# 123140146
# PBO PRAKTIKUM RD
# WEEK 3 #Tugas 3

from abc import ABC, abstractmethod

# Kelas Abstrak
class Animal(ABC):
    def __init__(self, name, age):
        if not name:
            raise ValueError("Nama hewan tidak boleh kosong.")
        if age < 0:
            raise ValueError("Usia hewan tidak boleh negatif.")
        
        self.__name = name      # Enkapsulasi
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @abstractmethod
    def make_sound(self):
        pass

    def info(self):
        return f"{self.__class__.__name__} bernama {self.__name}, usia {self.__age} tahun."

# Kelas Turunan (Inheritance + Polimorfisme)
class Lion(Animal):
    def make_sound(self):
        return "Roaarr!!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpettt!"

class Penguin(Animal):
    def make_sound(self):
        return "Gawk gakwk!"

class Dog(Animal):
    def make_sound(self):
        return "Guk guk!"

# Zoo Management System
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Hanya objek turunan dari Animal yang bisa ditambahkan.")
        self.animals.append(animal)

    def show_all_animals(self):
        if not self.animals:
            print("Kebun binatang kosong.")
        else:
            for animal in self.animals:
                print(animal.info())
                print("Suara:", animal.make_sound())
                print("-" * 30)

# Contoh penggunaan
if __name__ == "__main__":
    zoo = Zoo()
    try:
        zoo.add_animal(Lion("Simba", 5))
        zoo.add_animal(Elephant("Dumbo", 10))
        zoo.add_animal(Penguin("Skipper", 3))
        zoo.add_animal(Dog("Kaiser", 4))
        
        # Error Handling contoh
        # zoo.add_animal(Lion("", 3))        # Akan error karena nama kosong
        # zoo.add_animal(Dog("Buddy", -1))   # Akan error karena usia negatif
        # zoo.add_animal("Bukan Hewan")      # Akan error karena bukan objek Animal

    except (ValueError, TypeError) as e:
        print("Terjadi kesalahan:", e)

    zoo.show_all_animals()
