# tomato
import time

class tomato:
  def __init__(self, name, strand, main_weapon): # tomato strand is like class: mage, warrior, etc
    self.name = name

name = input("[tomato]: enter name: ")
tomato = tomato(name)
print(f"[tomato]: initialized tomato with name [{tomato.name}]")
