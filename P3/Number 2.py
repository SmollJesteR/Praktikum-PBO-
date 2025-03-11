# Muhammad Royhan Alfitra
# 123140146
# RD
# Nomor 2

import random

class Father:
  def __init__(self, blood_types):
    self.blood_types = blood_types

class Mother:
  def __init__(self, blood_types):
    self.blood_types = blood_types

class Child:
  def __init__(self, father: Father, mother: Mother):
    self.inherit_alleles = (random.choice(father.blood_types), random.choice(mother.blood_types))
    self.blood_types = self.deter_blood_types()
  
  def deter_blood_types(self):
    alleles = set(self.inherit_alleles)
    if alleles == {'A'}:
      return "A"
    elif alleles == {'B'}:
      return "B"
    elif alleles == {'A', 'B'}:
      return "AB"
    elif alleles == {'O'}:
      return "A" if "A" in alleles else "B" if "B" in alleles else "O"
    else:
      return "Error"
  
  def __str__(self):
    return f"Golongan Darah Anak : {self.blood_types} (Alel diwariskan dari : {self.inherit_alleles})"
  
#Contoh Output  

bpk = Father("AO")
mak = Mother("AB")
target = Child(bpk, mak)
print(target)