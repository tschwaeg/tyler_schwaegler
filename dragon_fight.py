played = 0

wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

easy = "Easy"
medium = "Medium"
hard = "Hard"

while True:
    wizard_hp = 100
    elf_hp = 150
    human_hp = 200
    orc_hp = 250
    easy_dragon_hp = 200
    medium_dragon_hp = 400
    hard_dragon_hp = 600

    wizard_damage = 200
    elf_damage = 100
    human_damage = 50
    orc_damage = 60
    easy_dragon_damage = 10
    medium_dragon_damage = 25
    hard_dragon_damage = 50

    played = played + 1
    print("Welcome to The Warriors Game")
    while True:
        print("1)   " + wizard)
        print("2)   " + elf)
        print("3)   " + human)
        print("4)   " + orc)
        character = input("Choose your character:")
        character = character.lower()
        if character == "1" or character == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character == "2" or character == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character == "3" or character == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if character == "4" or character == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        print("Unknown character, please try again.")

    print("\nYou chose: " + character)
    print(character + " hp: " + str(my_hp))
    print(character + " damage: " + str(my_damage) + "\n")

    while True: 
        print("Difficulty")
        print("1)   " + easy)
        print("2)   " + medium)
        print("3)   " + hard)
        difficulty = input("Choose the difficulty of your Dragon battle:")
        difficulty = difficulty.lower()
        if difficulty == "1" or difficulty == "easy":
            difficulty = easy
            dragon_hp = easy_dragon_hp
            dragon_damage = easy_dragon_damage
            break
        if difficulty == "2" or difficulty == "medium":
            difficulty = medium
            dragon_hp = medium_dragon_hp
            dragon_damage = medium_dragon_damage
            break
        if difficulty == "3" or difficulty == "hard":
            difficulty = hard
            dragon_hp = hard_dragon_hp
            dragon_damage = hard_dragon_damage
            break
    print("It is time to fight the Dragon! The difficulty of your Dragon battle is", difficulty, "and the Dragon has", dragon_hp, "hp and causes", dragon_damage, "hp damage per attack.\n")

    while True:
        dragon_hp -= my_damage
        print("The", character, "attacked the Dragon! The Dragon lost", my_damage, "hp.")
        print("The Dragon has", dragon_hp, "hp", "remaining.\n")
        if dragon_hp <= 0:
            print("The Dragon lost the battle!\n")
            break

        my_hp -= dragon_damage
        print("The dragon attacked the", character, "and", "the", character, "lost", str(dragon_damage), "hp.")
        print("The " + character + " has " + str(my_hp) + " hp remaining.\n")

        if my_hp <= 0:
            print("The", character, "has lost the battle!\n")
            break

    if played == 1:
        print("You have played", played, "time.")
    else:
        print("You have played", played, "times.")
    
    while True:
        again = input("Would you like to play again?")
        again = again.lower()
        if again == "yes" or again == "y":
            break
        if again == "no" or again == "n":
            break
        else:
            print("I didn't get that... would you like to play again?")
    if again == "yes":
        continue
    if again == "no":
        break
print("You have successfully ended your game session. You played", played, "times.")