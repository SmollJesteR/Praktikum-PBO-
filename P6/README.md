
# 🧪 Praktikum PBO - Modul 6: Login & Register System (Tkinter + OOP)

## 📌 Deskripsi Umum

Modul ini terdiri dari dua bagian utama yang dibuat menggunakan **Python Tkinter** dan konsep **OOP (Object-Oriented Programming)**:

1. 🔐 **Login System**
2. 📝 **Register System** (modifikasi dari Login System)

Tujuannya adalah membiasakan diri membuat **GUI** sederhana dengan *form*, validasi data, serta penggunaan class dan method.

---

## 1️⃣ Login System

### 🎯 Fitur:
- Form login dengan username & password
- Validasi login terhadap data bawaan (`self.users`)
- Pesan sukses dan gagal saat login

### 🖼️ Tampilan:
> Form login terdiri dari 2 input:  
> ✅ Username  
> ✅ Password  

### ⚙️ Cara Kerja:
```python
if username in self.users and self.users[username] == password:
    # login sukses
else:
    # login gagal
```

---

## 2️⃣ Register System

### 🆕 Fitur Tambahan:
- Tombol **Register** yang membuka jendela baru (`Toplevel`)
- Input tambahan: **Konfirmasi Password**
- Validasi: username unik & password cocok
- Menyimpan data user ke dictionary sementara (`self.users`)

### 📋 Langkah Pendaftaran:
1. Isi username dan password
2. Ulangi password di kolom *Confirm*
3. Klik **Submit**
4. 🎉 Jika berhasil, pengguna bisa login dengan akun baru!

---

## 💡 Bonus & Nilai Ekstra

✅ Menggunakan `Toplevel` window  
✅ Validasi lengkap (username unik, password match, field tidak boleh kosong)  
✅ Pemisahan kode jadi OOP yang rapi dan terstruktur  

---

## ▶️ Cara Menjalankan

Jalankan dengan Python 3:
```bash
python login_app.py
```

---


## 📦 Dependencies

- Python 3.x
- Modul `tkinter` (bawaan Python)

---

## 🎉 Penutup

Dengan latihan ini, kita sudah selangkah lebih dekat untuk bikin aplikasi desktop Python sendiri! 🚀
