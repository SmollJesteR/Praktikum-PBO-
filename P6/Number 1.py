import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Skibidi")
        self.master.geometry("600x300")
        self.master.resizable(False, False)

        self.lbl_username = tk.Label(master, text="Username:")
        self.lbl_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.ent_username = tk.Entry(master)
        self.ent_username.grid(row=0, column=1, padx=10)

        self.lbl_password = tk.Label(master, text="Password:") 
        self.lbl_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.ent_password = tk.Entry(master, show="*")
        self.ent_password.grid(row=1, column=1, padx=10)

        self.btn_login = tk.Button(master, text="Login", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=10)
    
    def login(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        if username == "Rusdi" and password == "123":
            messagebox.showinfo("Login Successful", "Welcome to Skibidi!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()