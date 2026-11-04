starting_energy = 3

choice = input("do you want to explore mystry island.(yes/no):")
if choice == "yes":
  print("welcome player")
  while starting_energy > 0:
    print("you are exploring mystry island")
    starting_energy -= 1
    print("energy finished game over")
else:
  print("good bye player")
    

