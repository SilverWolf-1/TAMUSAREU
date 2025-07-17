import random
import sys
from termcolor import colored

animales=["CHANGO","AGUILA","VIBORA","VENADO","JIRAFA","CONEJO","PAJARO","IGUANA","MEDUSA","DELFIN","CERDOS","COYOTE","PERROS","ARAÑAS","JAGUAR"] #list of animals in spanish compiled by Student A

comida=["POZOLE","MENUDO","FLANES","TOCINO","PASTEL","TORTAS","CONCHA","MANGOS","CEREZA","HUEVOS","PUERCO","PIPIÁN","CHIVAS","FLAUTA","TOMATE"] #list of food in spanish compiled by Student B 

artículos_cotidianos=["CHAMPÙ","DINERO","ESPEJO","MEDIAS","TOALLA","CAMISA","CORRAL","LLAVES","COPITA","LOCIÒN","ROPAJE", "GAVETA","PUERTA","COBIJA","SILLÒN"]#list of everyday items in spanish compiled by Student C

def print_menu():
  print("Wordle Infinito (Versión Español)")
  print("Con el teclado escribe una palabra de 6 letras.\n") 
  print("Leyenda:Si la letra es verde es correcto y esta en el espacio correcto, \n si la letra es amarilla la letra es correcta, pero no esta en el espacio correcto,\nsi no hay cambio la letra no esta en la palabra correcta. ")

def validacion():
  for i in range( min(len(guess), 6) ):
      if guess[i] == palabra[i]:
        print(colored(guess[i], 'green'), end="")
      elif guess[i] in palabra:
        print(colored(guess[i], 'yellow'), end="")
      else:
        print(guess[i], end="")
  

def read_random_word():
  
  palabras=random.choice(animales) or random.choice(comida) or random.choice(artículos_cotidianos)
  return palabras
    
print_menu()

otra_vez=""

while otra_vez != "s":
  palabra = read_random_word()
  for attempt in range(1,7):
    guess=input().upper()
    
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

    validacion()
    print()
    
    if guess == palabra:
      print(colored(f"Genial!!! En  {attempt} intentos aggarastes el WORDLE.", "light_blue"))
      break
    elif attempt==6:
      print(f"La respuesta era",palabra)
  otra_vez=input("Otra vez? Presiona S en el teclado para salir. Y presiona ENTER para ir a una ronda nueva.") 