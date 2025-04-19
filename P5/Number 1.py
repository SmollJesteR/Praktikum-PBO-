# MUHAMMAD ROYHAN ALFITRA
# 123140146
# SOAL 1

import random

class MineSweeper:  # Nama class sudah benar
    def __init__(self):
        self.board = [[False for _ in range(3)] for _ in range(3)]
        self.revealed = [[False for _ in range(3)] for _ in range(3)]  # Perbaikan nama atribut
        self.remaining_safe = 8  # Perbaikan nama variabel

        bomb_row = random.randint(0, 2)
        bomb_col = random.randint(0, 2)
        self.board[bomb_row][bomb_col] = True

    def display(self):  # Tetap menggunakan nama display
        for r in range(3):
            row_display = []
            for c in range(3):
                if self.revealed[r][c]:
                    row_display.append('X' if self.board[r][c] else 'O')
                else:
                    row_display.append('?')
            print(' '.join(row_display))

    def play(self):
        while True:
            self.display()  # Diubah sesuai nama method

            # Input validation loop
            while True:
                try:
                    row = int(input("Pilih baris (1-3): ")) - 1
                    col = int(input("Pilih kolom (1-3): ")) - 1

                    if 0 <= row < 3 and 0 <= col < 3:
                        if not self.revealed[row][col]:
                            break
                        else:
                            print("Kotak sudah dibuka!")
                    else:
                        print("Masukkan angka antara 1-3!")
                except ValueError:
                    print("Masukkan harus berupa angka!")

            # Process move
            self.revealed[row][col] = True

            if self.board[row][col]:
                self.display()
                print("Boom! Kamu kalah!")
                break
            else:
                self.remaining_safe -= 1
                if self.remaining_safe == 0:
                    self.display()
                    print("Selamat! Kamu menang!")
                    break

if __name__ == "__main__":
    game = MineSweeper()  # Diubah sesuai nama class
    game.play()