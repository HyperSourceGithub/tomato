# tomato
import time
import os

# tomato load
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
def tomato_load(rep):
    i = 0
    for tomato in range(rep):
        i = (i + 1) % len(symbols)
        print('\r\033[K%s loading tomato...' % symbols[i], flush=True, end='')
        time.sleep(0.1)

class tomato:
  def __init__(self, name, strand, main_weapon, secondary): # tomato strand is like class: mage, warrior, etc
    self.name = name
    self.strand = strand
    self.main = main_weapon
    self.side = secondary

tomato_load(30)
os.system('clear')
print("tomato loaded.")
name = input("[tomato]: enter name: ")
strand = input("[tomato]: enter strand (warrior (slice & dice), mage (majik), ranger (arrow dude), spy (sneaky), operative (secret government agent)): ").lower().strip()

# tomato get strand and define main
if strand == "warrior":
  print("[tomato]: selected class \"Warrior\"")
  main = "Sword"
elif strand == "mage":
  print("[tomato]: selected class \"Mage\"")
  main = "Staff"
elif strand == "ranger":
  print("[tomato]: selected class \"Ranger\"")
  main = "Crossbow"
elif strand == "spy":
  print("[tomato]: selected class \"Spy\"")
  main = "Silenced Pistol"
elif strand == "operative":
  print("[tomato]: selected class \"Operative\"")
  main = "Pistol"
else: 
  print("[tomato]: invalid option. defaulting to warrior.")
  strand = "warrior"
  main = "Sword"

side = input("[tomato]: enter a side weapon of your choice: ")

tomato = tomato(name, strand.capitalize(), main.capitalize(), side.capitalize())
print(f"[tomato]: initialized tomato with name [{tomato.name}], strand [{tomato.strand}], main [{tomato.main}], and side [{tomato.side}]")
