# 🧮 Python OOP Calculator & 🧬 Blood Type Inheritance

Welcome to this fun and educational Python repository! 🚀 Here, you'll find two exciting projects that showcase Object-Oriented Programming (OOP) in action:

1️⃣ **Simple Calculator with Dunder Methods** ➕➖✖️➗
2️⃣ **Blood Type Inheritance Simulation** 🩸

## 🧮 Simple Calculator Using Dunder Methods
This calculator takes advantage of Python’s **dunder methods** (a.k.a. magic methods) to perform operations like addition, subtraction, multiplication, division, exponentiation, and logarithms! 🧠✨

### 🎯 Features
- Implements OOP with operator overloading (`__add__`, `__sub__`, `__mul__`, etc.).
- Supports basic arithmetic operations (`+`, `-`, `*`, `/`, `^` for exponentiation).
- Includes logarithm calculation! 🏆
- Inspired by a `Point` class example to demonstrate dunder methods.

### ⚡ Example Usage
```python
calc1 = Calculator(10)
calc2 = Calculator(5)
print(calc1 + calc2)  # Output: 15
print(calc1 ^ calc2)  # Output: 100000 (10^5)
```

## 🔬 Blood Type Inheritance Simulation
This Python program simulates how blood types are inherited from parents to children. It randomly selects alleles and determines the child's blood type based on real genetic rules. 🧬

### 🎯 Features
- Utilizes OOP with three classes: `Father`, `Mother`, and `Child`.
- Randomly selects alleles from each parent.
- Determines the child's blood type based on genetic inheritance.
- Uses Python's `random.choice()` for realistic allele selection.

### 🏗️ How It Works
- `Father` and `Mother` classes store blood type alleles (e.g., "AO", "AB").
- `Child` class inherits one allele from each parent and determines its blood type.

### ⚡ Example Output
```
Golongan Darah Anak: A (Alel diwariskan dari: ('A', 'O'))
```

## 🚀 Installation & Running the Code
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/python-oop-projects.git
   ```
2. Navigate to the project folder:
   ```sh
   cd python-oop-projects
   ```
3. Run the desired Python script:
   ```sh
   python calculator.py   # For the calculator
   python inheritance.py  # For blood type inheritance
   ```

## 💡 Why This Project?
This project is perfect for:
✅ Learning **Object-Oriented Programming (OOP)** in Python.
✅ Understanding **genetics & inheritance** through code.
✅ Exploring **dunder methods & operator overloading** in Python.

## 🤝 Contributing
Want to improve or add more features? Feel free to fork this repository and submit pull requests! 🎉

## 📜 License
This project is open-source and available under the **MIT License**.

---

Thanks for checking out this project! Happy coding! 💻🎈

