# Input User
nama  = input("Masukkan Nama le : ")
nim   = input("Masukkan NIM : ")
waifu = input("Masukkan Nama Oshi Kamu Sekarang : ")

# Akses file me.txt
with open("Me.txt", "w") as file:
    file.write(f"Nama : {nama}\n")
    file.write(f"NIM : {nim}\n")
    file.write(f"Oshi : {waifu}\n")

# Check Parameter 
print("\nFile Me.txt telah berhasil dibuat!")