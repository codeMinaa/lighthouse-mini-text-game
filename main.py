starting_energy = 10
game_running = True

while game_running:
    print("MYSTERY ISLAND")
    print("1. explore island")
    print("2. check energy")
    print("3. leave game!")

    choice = input("choose an option: ")

    if choice == "1":
        if starting_energy > 0:
            print("you are exploring mystery island")
            starting_energy -= 1
            if starting_energy == "0":
              print("Energy Out!")
        else:
            print("you have no energy left!")

    elif choice == "2":
        print(f"Your energy is {starting_energy}")

    elif choice == "3":
        game_running = False
        print("leave game!")

    else:
        print("invalid choice. select 1, 2, or 3.")