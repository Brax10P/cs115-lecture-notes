
age = 27
age2 = 15

if age > 21:
  print("You are old.")
  print("You are an adult.")
else:
  print("You are young.")

difference = age-age2

if difference >= 0:
  print("Positive")
elif difference > 5:
  print("big number")
elif difference < 0:
  print("Negative")

if difference > 5: 
  print("big number")

counter = 0
while counter <= 10:
  print(counter)
  #counter = counter + 1
  counter += 1 #same thing


inventory = ['sword', 'shield', 'key']
for item in inventory:
  print(item)

# boolean operators
is_game_paused = False 
is_dead = False

if is_game_paused or is_dead:
  print("Game Paused")
else:
  print("Game not Paused")

if is_game_paused and is_dead:
  print("Game Over")

health = 50
if health == 0:
  is_dead = True
  