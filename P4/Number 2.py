# MUHAMMAD ROYHAN ALFITRA
# 123140146
# PBO PRAKTIKUM RD
# WEEK 3 #Tugas 2


class NotionWannabe:
  def __init__(self):
    self.tasks = []

  def add_task(self):
    task = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    if not task:
       # Penanganan error: input kosong
      print("Error: Tugas tidak boleh kosong.")
      return
    self.tasks.append(task)
    print("Tugas berhasil ditambahkan!")

  def del_task(self):
    if not self.tasks:
      # Penanganan error: tidak ada tugas yang bisa dihapus
      print("Daftar tugas kosong.")
      return
    try:
      nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
      if nomor < 1 or nomor > len(self.tasks):
         # Exception handling: input bukan angka yang valid
        raise IndexError
      tugas_dihapus = self.tasks.pop(nomor - 1)
      print(f"Tugas '{tugas_dihapus}' berhasil dihapus.")
    except ValueError:
      print("Error: Masukkan nomor yang valid.")
    except IndexError:
      # Exception handling: nomor tugas tidak sesuai dengan daftar
      print(f"Error: Tugas dengan nomor {nomor} tidak ditemukan.")

  def show_tasks(self):
    if not self.tasks:
      print("Daftar tugas kosong.")
    else:
      print("\nDaftar Tugas:")
      for i, task in enumerate(self.tasks, 1):
        print(f"{i}. {task}")
      print()

  def menu(self):
    while True:
      print("\nPilih aksi:\n")
      print("1. Tambah tugas")
      print("2. Hapus tugas")
      print("3. Tampilkan daftar tugas")
      print("4. Keluar")

      pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

      if pilihan == "1":
        self.add_task()
      elif pilihan == "2":
        self.del_task()
      elif pilihan == "3":
        self.show_tasks()
      elif pilihan == "4":
        print("Keluar dari program.")
        break
      else:
        print("Input tidak valid. Harap masukkan angka 1 sampai 4.")

    #Penjalanan Program

if __name__ == "__main__":
  app = NotionWannabe()
  app.menu()