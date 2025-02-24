# Struktur Piramida Segitiga
def seginiga(t):
    for i in range(1, t + 1):
        bin = "*" * (2 * i - 1)
        print(bin.center(2 * t - 1))

# Input Tinggi Piramida
t = int(input("Height : "))
seginiga(t)
