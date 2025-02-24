# Dictionary untuk murid
student = {}
total = int(input("Masukkan jumlah siswa: "))

# Loop Mengisi Dictionary
for i in range(total):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ").strip().title()
    nilai = int(input(f"Masukkan nilai untuk siswa {nama}: "))
    student[nama] = nilai

# Output kode
print("\nDictionary Siswa: ", student)