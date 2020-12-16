""" while loop and an if/else """

print("Welcome to MadLibs! In this program, you'll be prompted to enter certain words. At the end, "
    "a passage will be printed, filled with the words that you have inputted.")
flag = input("Ready to get started? Type 'yes' for yes and 'no' if not! ")

while flag == "yes":
    selection = input("You have 2 different types of MadLibs available. Type '1' for Vacation, '2' for Short Poem, and '0' to exit! ")
    if selection == "1":
        # execute vacation code
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        adjective3 = input("Enter a third adjective: ")
        
        bodyPart = input("Enter a part of the body: ")

        game = input("Enter a game: ")
        
        noun = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        noun3 = input("Enter a third noun: ")

        number = input("Enter a number: ")

        place = input("Enter a place: ")
        plant = input("Enter a plant: ")
        
        pluralNoun = input("Enter a plural noun: ") 
        pluralNoun2 = input("Enter another plural noun: ")
        pluralNoun3 = input("Enter a third plural noun: ")
        pluralNoun4 = input("Enter a fourth plural noun: ")
        
        verb = input("Enter a verb ending in ing: ")
        verb2 = input("Enter a second verb ending in ing: ")
        verb3 = input("Enter a third verb ending in ing: ")
        verb4 = input("Enter a fourth verb ending in ing: ")
        
        
        print("-----------------------------------")
        print("Vacations")
        print("-----------------------------------")
        print("A vacation is when you take a trip to some", adjective1, "place with your", adjective2, "family. "
            "Usually you go to some place that is near a/an", noun, "or up on a/an", noun2 +  ".",
            "A good vacation place is one where you can ride", pluralNoun, "or play", game, "or go hunting for", pluralNoun2 + ".",
            "I like to spend my time", verb, "or", verb2 + ".",
            "When parents go on a vacation, they spend their time eating three", pluralNoun3, "a day, and fathers play golf, "
            "and mothers sit around", pluralNoun4 + ".",
            "Last summer, my little brother fell in a/an", noun, "and got poison", plant, "all over his", bodyPart + ".",
            "My family is going to go to (the)", place, "and I will practice", verb4 + ".",
            "Parents need vacations more than kids because parents are always very", adjective3, "and because they have to work", number, "hours " 
            "every day all year making enough", pluralNoun4, "to pay for the vacation.")
        
        print("-----------------------------------")
    elif selection == "2":
        adjective = input("Enter an adjective: ")
        noun = input("Enter a plural noun: ")
        color = input("Enter a color: ")
        place = input("Enter a place: ")

        print("-----------------------------------")
        print("Roses are", adjective)
        print(noun, "are", color)
        print("Welcome to", place)
        print("It's great to have you here!") 
        print("-----------------------------------")
    elif selection == "0" :
        print("Thanks for playing!")
        break;
    else:
        print("Selection not recognized.")
    
    flag = input("Want to do it again? Enter 'yes' to keep going, and 'no' to quit! ")
