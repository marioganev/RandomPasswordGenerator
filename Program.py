while True:
    try:
        import os
        import time
        import random
        break
    except ImportError:
        quit()

#All of the combinations
low_password_body = ["python", "iphone", "mexico", "nice", "cry", "good", "bad", "weak", "strong", "data", "attack", "dish", "gym", "drama", "drive", "egg", "empty", "error", "fish", "flag", "flat", "focus", "food", "football", "soccer", "friend", "show", "free", "french", "fresh", "full", "run", "german", "grass", "blue", "red", "brown", "yellow", "purple", "pink", "orange", "pear", "hot", "cool", "tree", "car", "child", "eyes", "cannotbe", "what", "apple", "cookie", "carrot", "woman", "pizza", "lol", "after", "dark", "dog", "three", "world", "easy", "hard", "smile", "code", "hour", "hack", "eat", "pro", "fight", "battle", "music", "know", "need", "ask", "face", "age", "again", "cat", "chair", "table", "class", "coffee", "think"]

moderate_password_body = ["mYcat", "oVal", "doritSO", "HobBit", "piNeaPple", "whAtiN", "puPpYlOver", "feEtMan", "pUllminT", "sEveN", "neVertAke", "wHymUstYou", "bEreMember", "lOlcAtRun", "EroPeN" "wHrEan", "dRopMe"]

high_password_body = ["iHaveAbAs", "nEverMinddMe", "pErBinerAl", "fOrkAndPinecOne", "feAtNur", "OrabIaNo", "oPerTunEiN", "RukkOUsiNa", "pInerIne", "yUirIN", "tRubUinO", "oGErCuHog", "ljUfNAoi", "oGoodLiCed", "pREaNoip", "olMoOseRuCL", "FeAnOpIne", "OrEnnAo", "F0Rtn!T3"]

low_password_ending = ["52", "56", "72", "3", "89", "32", "96", "64", "33", "76", "43", "48", "68", "11", "9", "31", "41", "95", "55", "33", "99", "88", "66", "22"]

moderate_password_ending = ["@8*2", "#65%", "*67", "954", "42", "&683%", "%46#2", "97%1@", "5#$@", "32#%", "9&#&", "$#2@", "32&@", "$%31", "7%7", "89##$", "64#$%"]

high_password_ending = ["#*4@1!", "!5$#", "567&" , "6$83%", "6@#1", "67%*4!", "9%$4", "56$43@", "$#4524", "@#$23$@", "35$%@%#", "&*789", "@#$4%4", "45$%#", "$@2452", "34#%$@", "34@#$"]

complexity = input("Choose complexity level: (high, moderate, low): ")

if complexity == "high":
    print("Generating high-level password...")
    password_body_high=random.choice(high_password_body)
    password_endings_high=random.choice(high_password_ending)
    print("Your password is: " + password_body_high + password_endings_high)
    save_to_file_high = input("Would you like to save it to a file? (y/n): ")
    full_pass_high = password_body_high + password_endings_high

    if save_to_file_high == "y":
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_high)
        file.close()
        print("Password saved as Saved_Password.txt")
        print("File saved successfully!")


if complexity == "moderate":
    print("Generating moderate-level password...")
    password_body_moderate=random.choice(moderate_password_body)
    password_endings_moderate=random.choice(moderate_password_ending)
    print("Your password is: " + password_body_moderate + password_endings_moderate)
    save_to_file_moderate = input("Would you like to save it to a file? (y/n): ")
    full_pass_moderate = password_body_moderate + password_endings_moderate

    if save_to_file_moderate == "y":
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_moderate)
        file.close()
        print("Password saved as Saved_Password.txt")
        print("File saved successfully!")

if complexity == "low":
    print("Generating low-level password...")
    password_body_low=random.choice(low_password_body)
    password_endings_low=random.choice(low_password_ending)
    print("Your password is: " + password_body_low + password_endings_low)
    save_to_file_low = input("Would you like to save it to a file? (y/n): ")
    full_pass_low = password_body_low + password_endings_low

    if save_to_file_low == "y":
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_low)
        file.close()
        print("Password saved as Saved_Password.txt")
        print("File saved successfully!")
