from random import randint
from math import sqrt

width=10
height=10

key_x=randint(0,height)
key_y=randint(0,width)

player_x=randint(0,height)
player_y=randint(0,width)

player_foud_key=False

steps=0

distance_before_move=sqrt((key_x-player_x)**2+(key_y-player_y)**2)

while not player_foud_key:
  print("Poruszaj się za pomocą wsad by znaleźć klucz ")
  steps+=1
  move=input('Dokad idziesz? ')
  match move:
    case 'a':
      player_y -= 1
      if player_y < 0:
        print(f'Uderzasz w ścianę. Maksymalne wymiary piwnicy to {width} na {height}')
        player_y=0
    case 'd':
      player_y += 1
      if player_y > width:
        print(f'Uderzasz w ścianę. Maksymalne wymiary piwnicy to {width} na {height}')
        player_y=width
    case 'w':
      player_x += 1
      if player_x > height:
        print(f'Uderzasz w ścianę. Maksymalne wymiary piwnicy to {width} na {height}')
        player_x=height
    case 's':
      player_x -= 1
      if player_x < 0:
        print(f'Uderzasz w ścianę. Maksymalne wymiary piwnicy to {width} na {height}')
        player_x=0
    case 'q':
      quit()
    case '_':                                                                               #wszystko inne znak podłogi
      print('NIe wiem dokąd idziesz')
      continue

  print(f'Twoja aktualna pozycja X= {player_x} Y= {player_y}')

  distance_after_move=sqrt((key_x-player_x)**2+(key_y-player_y)**2)
  if distance_before_move>distance_after_move:
    print('Cieplej')
  else:
      print('Zimno')

  if player_x==key_x and player_y==key_y:
    print(f'Udało Ci się znaleźć klucz. Gratulacje /n Wykonałeś {steps} ruchów ')
    quit()
