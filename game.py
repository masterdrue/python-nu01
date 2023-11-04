#Task1
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damage = 100

human = "Human"
human_hp = 150
human_damage = 20

dragon_hp = 300
dragon_damage = 50

#Task 2 & 3
while True:
    while True:
        print("1)  Wizard")
        print("2)  Elf")
        print("3)  Human")

        choice = input("Choose your Dude: ").lower()

        if choice == "1" or choice == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break

        if choice == "2" or choice == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break

        if choice == "3" or choice == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break

        print("Stop being stupid and select a number")

    print("You selected: ", character)
    print("Health: ", my_hp)
    print("Damage" , my_damage)

    #Task4

    while True:
        dragon_hp = dragon_hp - my_damage
        print("the", character, "damaged the Dragon")
        print("The dragons hitpoints arew now: ", dragon_hp)
        
        if dragon_hp <= 0:
            print("The dragon has been defeated")
            break
        
        my_hp = my_hp - dragon_damage
        print("the dragon strikes back at", character)
        print("the", character + "'s hitpoints are not:", my_hp)
        print("")

        if my_hp <= 0:
            print("the", character, "is a loser" )
            break

    play_again = input("Play again? (y/n) :").lower()
    if play_again == 'n':
        print("Later Dude")
        break