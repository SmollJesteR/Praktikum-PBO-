# Muhammad Royhan Alfitra
# 123140146
# RD
# Nomor 1

import math

class kalku:
  def __init__(self, val):
    self.val = val
  
  def __add__(self, other):
    return kalku(self.val + other.val)
  
  def __sub__(self, other):
    return kalku(self.val - other.val)
  
  def __mul__(self, other):
    return kalku(self.val * other.val)
  
  def __truediv__(self, other):
    if other.val == 0:
      raise valerror("Operasi tidak dapat dilakukan")
    return kalku(self.val / other.val)
  
  def __pow__(self, other):
    return kalku(self.val ** other.val)
  
  def log(self):
    if self.val <= 0:
      raise valerror("Operasi tidak dapat dilakukan")
    return kalku(math.log(self.val))
  
  def __str__(self):
    return str(self.val)

# Output Hasil

a = kalku(10)
b = kalku(5)

print("Operasi Penjumlahan : ", (a + b))
print("Operasi Pengurangan : ", (a - b))
print("Operasi Perkalian : ", (a * b))
print("Operasi Pembagian : ", (a / b))
print("Operasi Perpangkatan : ", (a ** b))
print("Operasi Logaritma : ", (a.log()))