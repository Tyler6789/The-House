import time
import sys
# declaring global variable for number of keys in player's inventory #
number_of_keys = 0
# declaring global variables for room keys#
room1_key = 1
room2_key = 1
room3_key = 1
room4_key = 1
room5_key = 1
room6_key = 1
room7_key = 1
room8_key = 1
room9_key = 1

#function to delay text so that it feels a little more natural to read#
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

#handle all inventory items for the player#
def PlayerKeyInventory():
    global number_of_keys
    if number_of_keys <= 6:
        print("You pocket the key.")
        number_of_keys = number_of_keys + 1
        print("You have ", number_of_keys, "keys.")
    else:
        print("You have all the keys")




#Room 1 function#
def room1():
    global room1_key
    delay_print("""You awake with a start and fight the urge to scream as your brain scrambles to make sense of where you are.
    \nAs your eyes adjust to the dim light you peer about you to see you are in a room and you aren't sure how you arrived there...\n""")
    time.sleep(1)
    print()
    delay_print("A circular pool emanating whispers is set into the floor at the center, though you're not sure you care for a DRINK or a SWIM.")
    delay_print("  A small fluorescent light hangs limply from the ceiling and bathes\n the room in a dim, cold light.  A cracked, ugly wooden door is set to the EAST and a smooth black door is to the SOUTH.")
    time.sleep(1)
    print()
    delay_print("""\nOn the WEST wall stands an enormous door, ornately carved in stone, and set in its face are seven keyholes.  A NOTE is pinned to the wall next to it," and resting next to the note are the bones of a human long passed from this plane. The SKULL smiles blankly at you,"you think you see something glinting inside its mouth.\n""")
    time.sleep(2)
    room = 'one'
    while room == "one":
        answer = input("What would you like to do? ")
        if answer.upper() == "EAST":
            delay_print("\nThe door creaks loudly as you step through into the next room")
            time.sleep(2)
            room2()
        elif answer.upper() == "SOUTH":
            delay_print("\nYou reach forward to open the door, but the doorknob is missing, it won't budge.")
            continue
        elif answer.upper() == "WEST":
            delay_print("TODO")
        elif answer.upper() == "SKULL":
                action = input("The skull is aged and covered lightly in moss, you see something inside its MOUTH")
                if action.upper() == "MOUTH" and room1_key == 1:
                    room1_key -= room1_key
                    print("You struggle a moment to pull the jaws of the skull apart, and then it pops open with a creak. You reach in and pull the key free.")
                    PlayerKeyInventory()
                    time.sleep(3)
                    continue
                else:
                    print("The skull's mouth gapes at you.")
                    continue
        elif answer.upper() == "NOTE":
            print("")
  
        elif answer.upper() == "DRINK":
            delay_print("\nYou start to feel woozy and the room tilts slowly around you.  The whispers crescendo slightly and quietly beckon you forward.")
            delay_print("\nDespite your best efforts you tilt forward and the last think you feel before the darkness envelopes you is many hands gripping you to drag you to the depths below...")
            time.sleep(2)
            delay_print("\nYOU DIED")
            player_continue = input("\nContinue? YES or NO\n")
            if player_continue.upper() == "YES":
                room1()
            elif player_continue.upper() == "NO":
                print("Thanks for playing. The House will await your return...")
                break
            else:
                print("Choose YES or NO")
                continue
        else:
            print("You aren't really sure what to do, but it definitely wasn't that.")
            time.sleep(2)
            continue


def room2():
    room = "two"
    delay_print(
        """\nA dining table takes up almost the entirety of the room. There are six settings at the table, but all but one are piled high with rotting food. 
        The last plate holds a single key. The walls are far, far too high for a regular room and covered with drab, peeling wallpaper.  
        They continue up until you can no longer see them.  In the corner stands someone, they are tall enough that you cannot see past their shoulders. 
        Soft, long, rattles of breath emanate from above.""")
    time.sleep(2)
    print()
    print("BACK the way you came, or through the TRAP DOOR")
    answer = input()
    while room == "two":
        if answer.upper() == "BACK":
            delay_print("You walk back the way you came")
            room1()


def room3():
    print("""Filled with chairs of all types and sizes. Some chintzy and plush, others wooden and bare.  The room is dimly lit by a TV in the
     corner. A TV REMOTE sits on a small end table next to an abnormally large, faded Lazy boy. Its back is to the door, but you swear someone
      is sitting in it. Just inside the doorway is a LIGHT SWITCH.""")


def room4():
    delay_print("""A small bathroom with a dingy stand-up shower in the corner.  The shower is running and steam curls over the door, 
    pooling on the floor and becoming a dense fog.  You cannot see through the condensation but several forms undulate in wild patterns, 
    slithering together and apart in grotesque shapes. A MIRROR hangs above the sink and you see another door to the SOUTH.""")


def room5():
    delay_print("You look down the corridor and see the walls stretch out into darkness, a faint sniffling can be heard.")
    time.sleep(2)
    delay_print("Would you like to go FORWARD or BACK?")


def room6():
    delay_print("""You step into a cavernous room and are immediately stuck by the immense size of the space.  Every inch of the walls are 
    covered by a painting of the exact same figure. The floor is bare except for one chair placed in the middle.  
    A slender figure huddles in the chair, covering their face. You aren't sure, but the paintings might be of them…""")


def room7():
    print("TODO")


def room8():
    print("TODO")


def room9():
    print("TODO")

print("""  
           
==============================================================================================
        ___       ___                   ___                                                
       (   )     (   )                 (   )                                               
        | |_      | | .-.     .--.      | | .-.     .--.    ___  ___      .--.      .--.   
       (   __)    | |/   \   /    \     | |/   \   /    \  (   )(   )   /  _  \    /    \  
        | |       |  .-. .  |  .-. ;    |  .-. .  |  .-. ;  | |  | |   . .' `. ;  |  .-. ; 
        | | ___   | |  | |  |  | | |    | |  | |  | |  | |  | |  | |   | '   | |  |  | | | 
        | |(   )  | |  | |  |  |/  |    | |  | |  | |  | |  | |  | |   _\_`.(___) |  |/  | 
        | | | |   | |  | |  |  ' _.'    | |  | |  | |  | |  | |  | |  (   ). '.   |  ' _.' 
        | ' | |   | |  | |  |  .'.-.    | |  | |  | '  | |  | |  ; '   | |  `\ |  |  .'.-. 
        ' `-' ;   | |  | |  '  `-' /    | |  | |  '  `-' /  ' `-'  /   ; '._,' '  '  `-' / 
        `.__.    (___)(___)  `.__.'    (___)(___)  `.__.'    '.__.'     '.___.'    `.__.'  

==============================================================================================                                                                                    
                                                                                    """)
room1()
 
  