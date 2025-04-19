# 🎮 Mini Project: Simple Minesweeper & Hangman 🎉

Selamat datang di mini project *Game Sederhana* berbasis Object Oriented Programming (OOP) dengan Python! 🚀

---

## 📁 Struktur Proyek

```
├── simple_minesweeper.py   # Game Minesweeper 3×3 dengan 1 bom
├── simple_hangman.py      # Game Hangman dengan ASCII art fun
└── README.md              # Penjelasan kedua game ini
```

---

## 🏆 Requirement

1. **Minesweeper**
   - Papan berukuran 3 baris × 3 kolom.
   - Ada **1 bom** yang ditempatkan secara acak.
   - Simbol:
     - ❓ `?` → Kotak belum dibuka
     - ✅ `O` → Kotak sudah dibuka, **aman**
     - 💥 `X` → Kotak berisi **bom** dan sudah dibuka
   - Pemain kalah jika membuka kotak berisi bom.
   - Pemain menang jika berhasil membuka semua kotak aman.

2. **Hangman**
   - Pemain menebak huruf demi huruf untuk mengungkap kata rahasia.
   - Setiap kesalahan menambah satu tahap ASCII art *hangman*.
   - Daftar kata di-*load* secara acak dari array `words`.
   - Pemain kalah jika ASCII art selesai (tali habis 🤡).
   - Pemain menang jika berhasil menebak semua huruf sebelum kesempatan habis.

---

## 🚀 Cara Menjalankan

1. Pastikan Python 3.x sudah terpasang.
2. Clone atau unduh repository ini.
3. Buka terminal di folder proyek.

### Jalankan Minesweeper:
```bash
python simple_minesweeper.py
```

### Jalankan Hangman:
```bash
python simple_hangman.py
```

---

## 💡 Ringkasan Kode

### 1. simple_minesweeper.py
- **Kelas `Cell`**: Menyimpan status kotak (bom atau tidak, terbuka atau belum).
- **Kelas `Board`**: Membangun grid 3×3, menempatkan bom acak, membuka cell, cek menang/kalah, dan menampilkan papan.
- **Kelas `Game`**: Alur utama: input koordinat, panggil `board.reveal()`, tampilkan papan, dan cek kondisi.

### 2. simple_hangman.py
- **`stages`**: List ASCII art tahap demi tahap (7 tahap). 🎭
- **Fungsi `default_words()`**: Mengembalikan daftar kata teknikal.
- **Kelas `HangmanGame`**:
  - `self.secret`: Kata acak.
  - `self.guessed`: Set huruf yang telah ditebak.
  - `self.wrong`: Hitung kesalahan.
  - Metode `display_state()`: Cetak gambar + progress.
  - Metode `guess(ch)`: Validasi input, update state, beri feedback.
  - Metode `is_won()` & `is_lost()`: Cek akhir.
  - Metode `play()`: Looping permainan hingga selesai.

---

## 👍 Tips & Kustomisasi

- Tambahkan fitur **skor** atau **timer ⏱️**.
- Kembangkan ukuran papan Minesweeper (n×n) atau jumlah bom lebih banyak.
- Ubah ASCII art Hangman dengan gaya sendiri! 🖌️
- Buat tampilan GUI (Tkinter / PyGame).

---

## 📖 Lisensi

Distribusi bebas untuk keperluan belajar dan eksperimen. Selamat ber-coding! 💻✨

