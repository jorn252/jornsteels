#########################################start#############################################
mode2 = 0
category_secure = 0
print("For more info: whatsapp:+310610240195")
#################################system and disclaimer#############################################################
while mode2 == 0:
    single_multi = input("What do you want to play? singleplayer or multiplayer, type it in: ")
    if "single" in single_multi:
        mode2 += 2
        secret_word = ""
        guess = ""
        guess_count = 0
        out_of_guesses = False
        import random, time

        mode_secure = 1
        guess_limit = 3
        ###############################system single############################################################
        name = input("What is your name?: ").capitalize()
        print("")
        print("Hello " + name + " we are going to play a guessing game.")
        print("You need to guess the secret word.")
        print("")
        #######################################welcome###########################################################
        print("categories:")
        print("1.animals")
        print("2.provinces of the netherlands")
        print("3.pc parts")
        print("4.games")
        while category_secure == 0:
            cat = input("Which category do you want to play?: ")
            if "1" in cat:
                print("Ok")
                randani = random.randint(1, 10)
                category_secure += 1
                if randani == 0:
                    secret_word = "giraffe"
                elif randani == 1:
                    secret_word = "deer"
                elif randani == 2:
                    secret_word = "rabbit"
                elif randani == 3:
                    secret_word = "horse"
                elif randani == 4:
                    secret_word = "chicken"
                elif randani == 5:
                    secret_word = "cow"
                elif randani == 6:
                    secret_word = "sheep"
                elif randani == 7:
                    secret_word = "dolphin"
                elif randani == 8:
                    secret_word = "turtle"
                elif randani == 9:
                    secret_word = "ant"
                elif randani == 10:
                    secret_word = "pig"
            elif "2" in cat:
                randnat = random.randint(1, 10)
                category_secure += 1
                if randnat == 0:
                    secret_word = "zeeland"
                elif randnat == 1:
                    secret_word = "friesland"
                elif randnat == 2:
                    secret_word = "overijssel"
                elif randnat == 3:
                    secret_word = "groningen"
                elif randnat == 4:
                    secret_word = "flevoland"
                elif randnat == 5:
                    secret_word = "gelderland"
                elif randnat == 6:
                    secret_word = "utrecht"
                elif randnat == 7:
                    secret_word = "drenthe"
                elif randnat == 8:
                    secret_word = "limburg"
                elif randnat == 9:
                    secret_word = "noord-holland"
                elif randnat == 10:
                    secret_word = "noord-brabant"
            elif "3" in cat:
                randpc = random.randint(0, 10)
                category_secure += 1
                if randpc == 0:
                    secret_word = "psu"
                elif randpc == 1:
                    secret_word = "cpu"
                elif randpc == 2:
                    secret_word = "ram"
                elif randpc == 3:
                    secret_word = "gpu"
                elif randpc == 4:
                    secret_word = "epu"
                elif randpc == 5:
                    secret_word = "rgb"
                elif randpc == 6:
                    secret_word = "volt"
                elif randpc == 7:
                    secret_word = "wat"
                elif randpc == 8:
                    secret_word = "display"
                elif randpc == 9:
                    secret_word = "laptop"
                elif randpc == 10:
                    secret_word = "pc"
            elif "4" in cat:
                randgame = random.randint(0, 10)
                category_secure += 1
                if randgame == 0:
                    secret_word = "minecraft"
                elif randgame == 1:
                    secret_word = "roblox"
                elif randgame == 2:
                    secret_word = "overwatch"
                elif randgame == 3:
                    secret_word = "csgo"
                elif randgame == 4:
                    secret_word = "ark"
                elif randgame == 5:
                    secret_word = "recore"
                elif randgame == 6:
                    secret_word = "fifa"
                elif randgame == 7:
                    secret_word = "f1"
                elif randgame == 8:
                    secret_word = "gta"
                elif randgame == 9:
                    secret_word = "apex"
                elif randgame == 10:
                    secret_word = "cs"
            else:
                print("That is not a valid category, Please try again")
            print("")
        ######################################categories################################################################
        print("Choose your difficulty:")
        time.sleep(1)
        print("1.easy")
        time.sleep(1)
        print("2.medium")
        time.sleep(1)
        print("3.hard")
        time.sleep(1)
        print("4.extremely hard")
        time.sleep(1)
        print("")
        while mode_secure == 1:
            time.sleep(1)
            mode = input("Which mode do you want to play? type te number and press enter: ")
            if mode == "1":
                guess_limit = 8
                mode_secure = 2
            elif mode == "2":
                guess_limit = 5
                mode_secure = 2
            elif mode == "3":
                guess_limit = 3
                mode_secure = 2
            elif mode == "4":
                guess_limit = 1
                mode_secure = 2
            else:
                print("That is not a valid mode, please try again.")
            print("")
            print("")
        ######################################mode########################################################################
        while guess != secret_word and not (out_of_guesses):
            if guess_count < guess_limit:
                print("guess count")
                print(guess_count)
                guess = input("Enter guess: ").lower()
                if guess != secret_word:
                    print("WRONG, Please try another word")
                    print("")
                    if guess == "":
                        print("Please enter your guess")
                        print("")
                        guess_count -= 1
                guess_count += 1
            else:
                out_of_guesses = True
        ############################################guessing#########################################
        if out_of_guesses:
            print("Out of guesses " + name + ", YOU LOSE!")
            time.sleep(2)
            print("")
            print("The secret word was " + secret_word + "")
        ##################################LOSE##########################################################
        else:
            print("YOU WIN!, Congratulations " + name + "!")
    ###################################WIN#########################################################
    ##################################singleplayer##################################################
    elif "multi" in single_multi:
        mode2 += 2
        import time

        mode_secure = 1
        secret_word_secure = 0
        guess_limit = 3
        guess_limit_secure = 0
        Print_secure = 0
        secret_word = ""
        guess = ""
        guess_count = 0
        out_of_guesses = False
        ##############################system###########################################################################
        name1 = input("Give me the name of the player who comes up with the word: ").capitalize()
        print("")
        while secret_word_secure == 0:
            secret_word = input(
                "Hello " + name1 + " Please put your own word in, Another player wil need to guess it to win: ").lower()
            if len(secret_word.split()) > 1:
                print("It must be a word")
            else:
                print("")
                print("Ok the secret word is " + secret_word + " ")
                secret_word_secure += 1
        ###############################secret word set#######################################
        while guess_limit_secure == 0:
            guess_limit = input("How manny chances do you give him/her : ")
            try:
                guess_limit = int(guess_limit)
                guess_limit_secure += 2
            except ValueError:
                print("That is not a valid number, Pleas try again")
                print("")
        ###################################difficulty######################################################
        hint = input("In which catogory does the word belong, This is used for a hint: ")
        print("")
        print("after the screen is cleared you have to get the other player then it is him / her to guess the word")
        time.sleep(2)
        ###########################################category#############################
        while Print_secure <= 500:
            print("")
            Print_secure += 1
        ##########################setup for te player#########################################################################
        time.sleep(1)
        name = input("What is your name?: ").capitalize()
        print("Hello " + name + " we are going to play a guessing game.")
        print("")
        print("" + name1 + " has thought up the word")
        print("The word belongs in the " + hint + " catogory")
        time.sleep(1)
        print("")
        print("")
        #################################info player################################################################################
        while guess != secret_word and not (out_of_guesses):
            if guess_count < guess_limit:
                print("guess count")
                print(guess_count)
                guess = input("Enter guess: ").lower()
                if guess != secret_word:
                    print("WRONG,please try another word")
                    print("")
                    if guess == "":
                        print("Please enter your guess")
                        print("")
                        guess_count -= 1
                guess_count += 1
            else:
                out_of_guesses = True
        ####################################guessing############################################################################
        if out_of_guesses:
            print("Out of guesses " + name + ",YOU LOSE!")
            time.sleep(2)
            print("The secret word was " + secret_word + "")
        else:
            time.sleep(2)
            print("YOU WIN!,congratulations " + name + "")
    else:
        print("That is not a valid mode,please try again.")
##############################################singleplayer/multiplayer########################################
tips = str(input('''Please put in tips, I`f you don't have them just press enter.
 If you want to add a line for another tip type your tip with a + on the end : '''))
if "+" in tips:
    tip1 = str(input("Please put in your other tip: "))
    print("You can only give two tips otherwise it is bad for jorn's ego")
print("")
file = open("Ratings.txt", "a")
rating = str(input("what rating would you give my script/game? based on your experience: "))
file.write("\n"+name+": " + rating + "\n" + tips + "\n" + tip1 + "\n")
file.close()
######################################rating##############################################################
input("press enter to exit")
