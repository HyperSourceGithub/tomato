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

class game:
    def __init__(self, randomthing):
        self.randomthing = randomthing
        self.lore = '''A long, long, long, l o n g, time ago, a simple adventurer going by the name of \"padtole the tadpole\" found a tomato holding a gun.
They then had a duel thing.
------------------------------------------
🍅🔫🐸🔫🍅 la la la pew pew aaa boom boom
------------------------------------------
It was won by the tomato.
-----------------------------------------
   _______________
  / ☠️ ☠️ ☠️ ☠️ ☠️ \
 | ☠️ ☠️ ☠️ R.I.P. |
 |   Padtole       |
 |   (Tadpole)     |
  \ ☠️ ☠️ ☠️ ☠️ ☠️ /
------------------------------------------
Since then, rivalries have existed between tomatoes and tadpoles.
YOUR TASK: walk through places and go pew pew. '''


# tomato tomahto calss
class tomato:
  def __init__(self, name, strand, main_weapon, secondary): # tomato strand is like class: mage, warrior, etc
    self.name = name
    self.strand = strand
    self.main = main_weapon
    self.side = secondary

gametomato = game(randomthing="tomato")
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
print('''Welcome to...
_________ _______  _______  _______ _________ _______ 
\__   __/(  ___  )(       )(  ___  )\__   __/(  ___  )
   ) (   | (   ) || () () || (   ) |   ) (   | (   ) |
   | |   | |   | || || || || (___) |   | |   | |   | |
   | |   | |   | || |(_)| ||  ___  |   | |   | |   | |
   | |   | |   | || |   | || (   ) |   | |   | |   | |
   | |   | (___) || )   ( || )   ( |   | |   | (___) |
   )_(   (_______)|/     \||/     \|   )_(   (_______)
A game of epic proportions.''')
print(gametomato.lore)

path = input("[tomato] choose path (forest, volcano, underground)").lower().strip()

while True:
  if path == "forest":
    pass
  elif path == "volcano":
    pass
  elif path == "underground":
    pass
  else:
     print("[tomato] bruh.")
     break
  