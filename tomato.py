# tomato
import time

class tomato:
  def __init__(self, name):
    self.name = name

name = input("[tomato]: enter name: ")
tomato = tomato(name)
print(f"[tomato]: initialized tomato with name [{tomato.name}]")
