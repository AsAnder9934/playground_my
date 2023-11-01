from random import randint

width=10
height=10

key_x=randint(0,height)
key_y=randint(0,width)

player_x=randint(0,width)
player_y=randint(0,height)

player_foud_key=False

while not player_foud_key:
  print("Poruszaj się za pomocą wsad by znaleźć klucz ")

  move=input('Dokad idziesz? ')
  match move:
    case 'a':
      player_y -= 1
    case 'd':
      player_y += 1
    case 'w':
      player_x += 1
    case 's':
      player_x -= 1

  print(f'Twoja aktualna pozycja X= {player_x} Y= {player_y}')
