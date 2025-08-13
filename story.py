from ascii_art import INTRO, TREASURE_CHEST, SKULL

def intro():
    print(INTRO)
    print("Welcome, brave adventurer!")
    print("You stand at the mouth of a dark cave, where legends say a great treasure is hidden.")
    print("Will you dare to enter?")
    print()

def stage_one():
    choice = input("Do you ENTER the cave or WALK away? (enter/walk): ").strip().lower()
    if choice == "enter":
        return "stage_two"
    else:
        print("You walk away... The treasure remains lost to the ages.")
        return "end"

def stage_two():
    print("\nThe cave is damp and echoes with strange sounds.")
    choice = input("You see two paths ahead — LEFT toward glowing crystals or RIGHT into the darkness. (left/right): ").strip().lower()
    if choice == "left":
        print("\nThe crystals glow... but behind them, you find a sleeping dragon! You quietly retreat.")
        return "stage_three"
    else:
        print("\nYou trip on a rock and fall into a pit...")
        print(SKULL)
        print("Game Over.")
        return "end"

def stage_three():
    print("\nYou follow the tunnel until you reach a wooden chest covered in dust.")
    print(TREASURE_CHEST)
    choice = input("Do you OPEN the chest or LEAVE it? (open/leave): ").strip().lower()
    if choice == "open":
        print("\nInside you find gold, jewels, and priceless relics!")
        print("You are now the richest adventurer alive!")
    else:
        print("\nYou decide some treasures are better left untouched.")
    return "end"
