import time
import random
character_name = ""
friend_name = ""
toolsinshop = ["snowshoes", "ice axe", "rope", "crampons", "flashlight",
               "skis", "trekking poles", "shovel"]
backpack = []
namesforstranger = ['Lizzy', 'Jimmy', 'Sarah', 'Kaylee', 'Stephen', 'Carmel',
                    'Alex', 'Becky', 'Craig', 'Ben']
strangername = ""
accepthelp = ""


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def valid_input(text_input, valid_responses):
    while True:
        response = input(text_input).lower()
        for option in valid_responses:
            if option in response and len(option) == len(response):
                return response
        print_pause("Sorry, I don't understand!")


def snowstorm():
    print_pause("***********************************")
    print_pause("********  ******* ********* *******")
    print_pause("*******    **** *** ****** * ******")
    print_pause("****** **** *  ***** **** *** *****")
    print_pause("***** ******  ******* ** ***** ****")
    print_pause("**** ******** ********  ******* ***")
    print_pause("*** ********** ******** ******** **")
    print_pause("** ************ ******** **********\n")


def play_again():
    global character_name
    global friend_name
    global toolsinshop
    global backpack
    global strangername
    global accepthelp
    print_pause("Would you like to play again?\n")
    play_again = valid_input("Type 'yes' or 'no'\n\n", ['yes', 'no'])
    if play_again == "yes":
        character_name = ""
        friend_name = ""
        toolsinshop = ["skis", "ice axe", "rope", "crampons", "flashlight"]
        backpack = []
        strangername = ""
        accepthelp = ""
        play_massif_rescue()
    if play_again == "no":
        print_pause("\nThank you for playing!")
        print_pause("This game was created by Corey Wright.")
        print_pause("Copyright: 2018 Massif Games LLC.")
        print_pause("ALL RIGHTS RESERVED.")
        print_pause("Designed in the USA.")


def game_intro():
    global character_name
    global friend_name
    global toolsinshop
    print_pause("")
    print_pause("   M A S S I F    R E S C U E  \n")
    snowstorm()
    print_pause("Welcome to the game 'Massif Rescue'! \n")
    print_pause("You are a mountaineer on a rescue mission \n"
                "to save your friend who is lost on Mt. Tila, \n"
                "a mountain full of treacherous glaciers.\n")
    character_name = input("Type a name for your character: \n\n")
    friend_name = input(f"\nType the name of the friend that {character_name} "
                        "is trying to save. \n\n")
    print_pause(f"\n{character_name} heads to the empty \n"
                f"Mt. Tila Ski Lodge to get gear and supplies.\n"
                f"{character_name} can barely see through the snowstorm.\n")
    print_pause(f"Walking into the lodge shop, {character_name} begins to \n"
                f"pack the tools needed for the rescue mission.\n")
    print_pause(f"However, after clothes, food, and water, \n"
                f"{character_name} only has enough room for 3 more items.\n")


def choose_tools():
    global backpack
    global toolsinshop
    tool1 = valid_input(f"What is the first tool {character_name} should take?"
                        f"\n\nHere are the tools you can choose from: \n"
                        f"{toolsinshop}\n\n", toolsinshop)
    backpack.append(tool1)
    toolsinshop.remove(tool1)
    print_pause(f"\n{character_name} adds the {tool1} to the pack.\n")
    tool2 = valid_input(f"What is the second tool {character_name} should take"
                        f"? \n\nHere are the tools you can choose from: \n"
                        f"{toolsinshop}\n\n", toolsinshop)
    backpack.append(tool2)
    toolsinshop.remove(tool2)
    print_pause(f"\n{character_name} adds the {tool2} to the pack.\n")
    tool3 = valid_input(f"What is the third tool {character_name} should take?"
                        f"\n\nHere are the tools you can choose from: \n"
                        f"{toolsinshop}\n\n", toolsinshop)
    backpack.append(tool3)
    toolsinshop.remove(tool3)
    print_pause(f"\n{character_name} adds the {tool3} to the pack.\n")


def change_tools():
    global backpack
    global toolsinshop
    global answer
    print_pause(f"\nHere are the tools in {character_name}'s' backpack:\n")
    print_pause(backpack)
    print_pause(f"\nWhich tool should {character_name} return to the shop?\n")
    tool = valid_input('', backpack)
    backpack.remove(tool)
    toolsinshop.append(tool)
    print_pause(f"\nHere are the tools available in the Ski Lodge:\n")
    print_pause(toolsinshop)
    print_pause(f"\nWhich tool should {character_name} take?\n")
    tool = valid_input('', toolsinshop)
    toolsinshop.remove(tool)
    backpack.append(tool)
    print_pause(f"Here are the tools currently in {character_name}'s backpack:"
                f"\n\n{backpack}")
    print_pause(f"\nShould {character_name} swap more tools?\n")
    answer = valid_input(f"Type 'Yes' or 'No':\n\n", ['yes', 'no'])
    if answer == "yes":
        change_tools()
    elif answer == "no":
        print_pause(f"\n{character_name} slowly climbs back to the crevasse \n"
                    f"where {friend_name} is stuck and slowly freezing to "
                    f"death!\n")
        print_pause("The snowstorm continues to howl...\n")
        snowstorm()
        rescue()


def you_lose():
    print_pause(f"A snowstorm came roaring down the mountain, encompassing "
                f"both {character_name} and {friend_name} in a sea of white.\n"
                )
    snowstorm()
    print_pause("A few days later, a search party found them, frozen like \n"
                "mummies, and stone-cold dead.\n")
    print_pause("You have lost the game of Massif Rescue.\n")
    play_again()


def leaving_lodge():
    global strangername
    global accepthelp
    strangername = random.choice(namesforstranger)
    print_pause(f"{character_name} leaves the lodge with the {backpack[0]}, \n"
                f"{backpack[1]}, and {backpack[2]}.\n")
    print_pause(f"Immediately, {character_name} meets another mountaineer "
                f"named {strangername}.\n")
    print_pause(f"{strangername} offers to help in the search for "
                f"{friend_name}.\n")
    print_pause(f"Should {character_name} accept {strangername}'s help?\n\n")
    accepthelp = valid_input(f"Type 'yes' or 'no':\n\n", ['yes', 'no'])


def no_rescue():
    print_pause(f"\nShould {character_name} head back to the store to "
                "get different gear?\n")
    rescueresponse = valid_input("Type 'yes' or 'no':\n\n", ['yes', 'no'])
    if rescueresponse == "yes":
        print_pause(f"\n{character_name} heads back to the store.\n")
        change_tools()
    elif rescueresponse == "no":
        print_pause(f"\n{character_name} leaves {friend_name} in the "
                    f"crevasse to die.\n")
        print_pause(f"Perhaps the mountain was watching, because...")
        you_lose()


def yes_rescue():
    print_pause(f"What tool should {character_name} use to "
                f"rescue {friend_name}?\n")
    print_pause(f"The '{backpack[0]}'', the '{backpack[1]}'', "
                f"or the '{backpack[2]}'?\n")
    rescue_tool = valid_input(f"Type the tool that {character_name} "
                              f"should use:\n\n", backpack)
    if rescue_tool == "rope":
        print_pause(f"{character_name} lowers the rope down the crevase, "
                    f"\nand pulls {friend_name} to safety!\n")
        luck = random.choice(['win', 'win', 'win', 'lose'])
        if luck == "lose":
            print_pause("Unfortunately...\n")
            you_lose()
        elif luck == "win":
            print_pause(f"They quickly head down the mountain, before the "
                        f"next snowstorm comes!\n")
            snowstorm()
            print_pause(f"Congratulations, {character_name} and {friend_name} "
                        f"are safe!\n")
            print_pause("You have won!\n")
            play_again()
    elif rescue_tool != "rope":
        print_pause(f"{character_name} lays down by the edge of the "
                    f"crevasse and stretches out the {rescue_tool} towards "
                    f"{friend_name}.\n")
        luck = random.choice(['win', 'lose', 'lose', 'lose', 'lose'])
        if luck == "lose":
            print_pause(f"Unfortunately, just as {friend_name} was "
                        f"stretching out to grab the {rescue_tool}, the edge "
                        f"of the crevasse cracked, and {character_name} fell "
                        f"into the crevasse and broke both legs.\n")
            you_lose()
        elif luck == "win":
            print_pause(f"{friend_name} grabs the {rescue_tool}, \n"
                        f"and is pulled to safety by {character_name}!\n")
            print_pause(f"They quickly head down the mountain, before the "
                        f"next snowstorm comes!\n")
            snowstorm()
            print_pause(f"Congratulations, {character_name} and {friend_name} "
                        f"are safe!\n")
            print_pause("You have won!\n")
            play_again()


def rescue():
    print_pause(f"Should {character_name} try to rescue {friend_name}?\n")
    answer = valid_input("Type 'yes' or 'no':\n\n", ['yes', 'no'])
    if answer == "no":
        no_rescue()
    elif answer == "yes":
        yes_rescue()


def crevase_from_stranger():
    print_pause(f"Miraculously, in spite of the fall, {character_name} "
                f"was not hurt.\n")
    print_pause(f"'I see you met the evil {strangername}' says "
                f"{friend_name}. \n")
    print_pause(f"'I was also pushed into the crevasse! I've lost "
                f"all my gear!'")
    if "crampons" in backpack and "ice axe" in backpack:
        print_pause(f"'Don't worry {friend_name}!' says {character_name}.\n")
        print_pause(f"'I'll use my crampons & ice axe to climb out, "
                    f"and then help you!'\n")
        print_pause(f"{character_name} climbs vertically to the "
                    f"top of the crevasse, \n"
                    f"then peers back down at {friend_name}.\n")
        rescue()
    elif "crampons" not in backpack and "ice axe" not in backpack:
        print_pause(f"Unfortunately, {character_name} did not have "
                    f"an ice axe or crampons.\n")
        print_pause(f"These tools are needed to climb out of a crevasse.\n")
        print_pause(f"{character_name} and {friend_name} were "
                    f"permanently stuck!\n")
        you_lose()
    elif "crampons" in backpack and "ice axe" not in backpack:
        print_pause(f"Unfortunately, {character_name} did not have "
                    f"an ice axe.\n")
        print_pause(f"Even with crampons, an ice axe is needed "
                    f"to climb out of a crevasse.\n")
        print_pause(f"{character_name} and {friend_name} were "
                    f"permanently stuck!\n")
        you_lose()
    elif "crampons" not in backpack and "ice axe" in backpack:
        print_pause(f"Unfortunately, {character_name} did not have "
                    f"crampons.\n")
        print_pause(f"Even with an ice axe, crampons are needed to "
                    f"climb out of a crevasse.\n")
        print_pause(f"{character_name} and {friend_name} were "
                    f"permanently stuck!\n")
        you_lose()


def climbing_mt():
    if accepthelp == 'yes':
        print_pause(f"\n{strangername} and {character_name} begin "
                    f"climbing the mountain.\n")
        print_pause(f"Soon they come to a great big crevasse.\n")
        print_pause(f"From deep inside the crevasse, they can hear \n"
                    f"{friend_name} calling for help!\n")
        print_pause(f"{character_name} turns to {strangername} to "
                    f"make a plan.\n")
        print_pause(f"{strangername} has an evil look!\n")
        print_pause(f"With a wicked laugh, {strangername} pushes \n"
                    f"{character_name} into the crevasse and runs away.\n")
        crevase_from_stranger()
    elif accepthelp == 'no':
        print_pause(f"\n{character_name} thanks {strangername} for the "
                    f"offer but politely declines.\n")
        print_pause(f"{character_name} begins climbing the mountain and "
                    f"comes to a big crevasse.\n")
        print_pause(f"From deep inside the crevasse, {friend_name} is "
                    f"calling for help!\n")
        print_pause(f"'Did you meet a stranger coming here?' "
                    f"asks {friend_name}. \n")
        print_pause(f"Someone named {strangername} pushed me into "
                    f"the crevasse! I've lost all my gear!\n")
        print_pause(f"'Yes', says {character_name}, 'but I left {strangername}"
                    f" to find you!'")
        print_pause(f"'I'm glad I did!\n\n")
        print_pause(f"{character_name} looks at the dangerous crevasse.")
        print_pause(f"The edge seems very dangerious.")
        rescue()


def play_massif_rescue():
    game_intro()
    choose_tools()
    leaving_lodge()
    climbing_mt()


play_massif_rescue()
