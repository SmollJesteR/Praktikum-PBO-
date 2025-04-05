# MUHAMMAD ROYHAN ALFITRA
# 123140146
# PBO PRAKTIKUM RD
# WEEK 3 #Tugas 1

import math

class Calc:
    def __init__(self):
        self.number = None

    def get_input(self):
        user_input = input("Masukkan angka : ")
        try:
            self.number = float(user_input)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")
            return False
        return True

    def verifikasi_input(self):
        if self.number < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
            return False
        elif self.number == 0:
            print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            return False
        return True

    def hitung_sqr(self):
        return math.sqrt(self.number)

    def run(self):
        while True:
            if not self.get_input():
                continue
            if not self.verifikasi_input():
                continue
            result = self.hitung_sqr()
            print(f"Akar kuadrat dari {self.number} adalah {result}")
            break

# Penjalanan Program
if __name__ == "__main__":
    calculator = Calc()
    calculator.run()
